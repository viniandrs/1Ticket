# Singleton utilizado para ler e escrever na planilha

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

import configReader

# Configuracao inicial do google cloud
SERVICE_ACCOUNT_FILE = 'service_account.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Conectando a planilha
try:
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
except HttpError as err:
    print(err)

sheetID = configReader.sheetID

# PRIVATE

# Busca as informacoes de um id na tabela
def p_getData(id_procurado):
    data = sheet.values().get(spreadsheetId=sheetID,
                                range="LISTA!a2:e").execute().get("values")

    for pessoa in data:
        id = pessoa[0]
        if id == id_procurado:
            return pessoa

    print("ID nao encontrado!")
    return 0

# Metodo para obter o ID da ultima linha da tabela
def getLastID():
    rows = sheet.values().get(spreadsheetId=sheetID,
                            range="LISTA!a2:e").execute().get("values")
    try:
        if not rows:
            return '0'

        last_row = rows[-1]
        last_id = last_row[0]
        return last_id
    
    except:
        print("error")
        exit()

# Metodo para adicionar um novo cliente a tabela
def addCostumer(id, email, phone):
    lastID = getLastID()
    newID = str(int(lastID)+2)
    new_row = [[id, email, phone, 0, 0]]
    request = sheet.values().update(spreadsheetId=sheetID,
                                    range="LISTA!a"+newID,
                                    valueInputOption="USER_ENTERED",
                                    body={"values": new_row})
    try:
        request.execute()
        print("Planilha atualizada com sucesso!\n")
    except:
        print("!!!!!!!!!!ERROR WRITING IN THE TABLE!!!!!!!!!!!")

# Printa as informacoes de um id
def readID(id_procurado):
    pessoa = p_getData(id_procurado)

    if pessoa != 0:
        print("ID: " + pessoa[0] + " / Email: " + pessoa[1] +\
                     " / Phone: " + pessoa[2])

# Atualiza o telefone de um id
def updatePhone(id, new_phone):
    row = int(id) + 1
    data = p_getData(id)
    data[2] = new_phone

    request = sheet.values().update(spreadsheetId=sheetID,
                                    range="LISTA!a"+str(row),
                                    valueInputOption="USER_ENTERED",
                                    body={"values": [data]})
    try:
        request.execute()
        print("Telefone atualizado com sucesso:")
        readID(id)
        print("\n")
    except:
        print("!!!!!!!!!!ERROR UPDATING PHONE !!!!!!!!!!!")

# Atualiza o email de um id
def updateEmail(id, new_email):
    row = int(id) + 1
    data = p_getData(id)
    data[1] = new_email

    request = sheet.values().update(spreadsheetId=sheetID,
                                    range="LISTA!a"+str(row),
                                    valueInputOption="USER_ENTERED",
                                    body={"values": [data]})
    try:
        request.execute()
        print("Email atualizado com sucesso!")
        readID(id)
    except:
        print("!!!!!!!!!!ERROR UPDATING EMAIL !!!!!!!!!!!")

