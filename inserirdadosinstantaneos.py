import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

import random

#uid = input("Insira o UID do cliente: ")

uid = 'h2fcw1fp08NY75fMn6HsuFwpOAC3'

# Carregue as credenciais do arquivo JSON baixado
cred = credentials.Certificate("C:/Users/jhonn/Documents/GitHub/SmartEnergy/smart-energy-695e0-firebase-adminsdk-22x50-10adce7a05.json")

# Inicialize o Firebase Admin SDK com as credenciais
firebase_admin.initialize_app(cred)

db = firestore.client()

print('usuarios/' + uid)

documento_ref = db.document('usuarios/' + uid)
print("Firebase Operante")

auxiliar = []


for i in range(210):
    
    if ((i % 24 == 0) and (i != 0)):
        
        # dados detalhados
        documento_ref = db.document('usuarios/' + uid + '/dias_anteriores/dados_detalhados')
        dados = {
            str(auxiliar[0]['data_hora']): {'consumo': auxiliar}
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


        media_gastos_por_comodo = []
        for comodo, total_gasto in total_gastos_por_comodo.items():
            contagem = contagem_por_comodo[comodo]
            media_gastos = total_gasto / contagem
            media_gastos_por_comodo.append(
                { 
                    'data_hora': auxiliar[0]['data_hora'],
                    'comodo': comodo,
                    'gasto': media_gastos
                }
            )
            
            
        
        
        # print('media_gastos_por_comodo: ', media_gastos_por_comodo)
        # print('total_gastos_por_comodo: ', total_gastos_por_comodo)
        
        dados = {
            str('media_' + auxiliar[0]['data_hora']): media_gastos_por_comodo
        }
        
        documento_ref.set(dados, merge=True)
        
        documento_ref = db.document('usuarios/' + uid)

        auxiliar = []
    
    for j in range(3):
        data_e_hora_formatadas = (datetime.datetime.now() + datetime.timedelta(hours=i)).strftime("%Y-%m-%d %H:%M:%S")
        
        if ((j % 3) == 0):
            comodo = "quarto"
        elif ((j % 3) == 1):
            comodo = "sala"
        else:
            comodo = "sacada"

        gasto = str(int(random.uniform(0, 4) + 1)) + " KWh"

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
    
    
print(auxiliar)
documento_ref.set(dados, merge=True)