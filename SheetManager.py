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

# Metodo para obter o ID da ultima linha da tabela
def getLastID():
    try:
        rows = sheet.values().get(spreadsheetId=sheetID,
                                range="LISTA!a2:d").execute().get("values")
        last_row = rows[-1]
        last_id = last_row[0]
        return last_id
    except:
        print("error")
        exit()

# Metodo para adicionar um novo cliente a tabela
def addCostumer(id, email):
    lastID = getLastID()
    newID = str(int(lastID)+2)
    new_row = [[id, email, 0, 0]]
    request = sheet.values().update(spreadsheetId=sheetID,
                                    range="LISTA!a"+newID,
                                    valueInputOption="USER_ENTERED",
                                    body={"values": new_row})
    try:
        request.execute()
        print("Planilha atualizada com sucesso!\n")
    except:
        print("!!!!!!!!!!ERROR WRITING IN THE TABLE!!!!!!!!!!!")
