import serial.tools.list_ports
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

# Carregue as credenciais do arquivo JSON baixado
cred = credentials.Certificate("smart-energy-695e0-firebase-adminsdk-22x50-10adce7a05.json")

# Inicialize o Firebase Admin SDK com as credenciais
firebase_admin.initialize_app(cred)

db = firestore.client()

documento_ref = db.document('usuarios/bYnzcmiYzU0o72I6dfdN')
print("Firebase Operante")

porta = "COM3"
baud = 9600
arquivo_nome = "logger.csv"

# Criando arquivo CSV
#arquivo = open(arquivo_nome,  "w", newline="") # parametro a cria se nn existir
#print("Criando arquivo CSV")

# abrindo a porta
ser = serial.Serial(porta, baud)
ser.flushInput()
print("Abrindo Serial")

auxiliar = [{}]

# lendo porta
while True:
    consumo = str(ser.readline().decode("utf-8")) #instrucao bloqueante
    print(consumo)
    comodo = consumo[:7]
    comodo = comodo.strip()
    gasto = consumo[7:]
    # Obtém a data e hora atuais e Formata a data e hora para exibição
    data_e_hora_formatadas = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    # Crie um objeto que deseja enviar para o Firestore
    
    auxiliar.append(
        {
        'data_hora': data_e_hora_formatadas,
        'comodo': comodo,
        'gasto': gasto
        }
    )
    dados = {
        'consumo': auxiliar,
        # Outros campos e valores
    }
    documento_ref.set(dados, merge=True)
    #arquivo.write(data_e_hora_formatadas + " " + consumo)

#arquivo.close()
ser.close()











