from pydoc import importfile
import SheetManager
import salesManager

def main():
    # Conectando-se à planilha
    SHEET_ID = SheetManager.sheetID
    sheet = SheetManager.sheet
    print("Planilha conectada com sucesso")

    # Descobrindo o último ID
    last_id = SheetManager.getLastID()

    print('Ingressos vendidos: '+last_id)
    key = int(input('1- Vender / 2- Consultar/ 3- Sair\n'))

    if key == 1:
        salesManager.sellTicket()
    elif key == 2:
        pass
    else:
        exit()     

while(1):
    main()