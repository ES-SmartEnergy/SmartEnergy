import serial.tools.list_ports
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

uid = input("Insira o UID do cliente: ")

# Carregue as credenciais do arquivo JSON baixado
cred = credentials.Certificate("smart-energy-695e0-firebase-adminsdk-22x50-10adce7a05.json")

# Inicialize o Firebase Admin SDK com as credenciais
firebase_admin.initialize_app(cred)

db = firestore.client()

documento_ref = db.document('usuarios/' + uid)
print("Firebase Operante")

porta = "COM3"
baud = 9600

# abrindo a porta
ser = serial.Serial(porta, baud)
ser.flushInput()
print("Abrindo Serial")

auxiliar = []

i = 0

while True:
    
    if ((i % 24 == 0) and (i != 0)):
        
        # dados detalhados
        documento_ref = db.document('usuarios/' + uid + '/dias_anteriores/dados_detalhados')
        dados = {
            str(auxiliar[0]['data_hora']): auxiliar
        }
        
        documento_ref.set(dados, merge=True)
        
        # dados brutos
        documento_ref = db.document('usuarios/' + uid + '/dias_anteriores/dados_brutos')

        total_gastos_por_comodo = {}

        contagem_por_comodo = {}

        for item in auxiliar:
            comodo = item['comodo']
            gasto = item['gasto']

            total_gastos_por_comodo[comodo] = total_gastos_por_comodo.get(comodo, 0) + int(gasto[:-4])

            contagem_por_comodo[comodo] = contagem_por_comodo.get(comodo, 0) + 1


        media_gastos_por_comodo = {}
        for comodo, total_gasto in total_gastos_por_comodo.items():
            contagem = contagem_por_comodo[comodo]
            media_gastos = total_gasto / contagem
            media_gastos_por_comodo[comodo] = media_gastos
        
        dados = {
            str('media' + auxiliar[0]['data_hora']): media_gastos_por_comodo
        }
        
        documento_ref.set(dados, merge=True)
        
        documento_ref = db.document('usuarios/' + uid)

        auxiliar = []
    
    consumo = str(ser.readline().decode("utf-8")) #instrucao bloqueante
    print(consumo)
    comodo = consumo[:7] # pega os primeiros 7 caracteres
    comodo = comodo.strip()
    gasto = consumo[7:] # tira os primeiros 7 caracteres

    data_e_hora_formatadas = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    auxiliar.append(
        {
        'data_hora': data_e_hora_formatadas,
        'comodo': comodo,
        'gasto': gasto
        }
    )
    dados = {
        'consumo': auxiliar,
    }
    
    i += 1
    
    print(auxiliar)
    documento_ref.set(dados, merge=True)
    
ser.close()