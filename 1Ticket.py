from pydoc import importfile
import SheetManager
import salesManager
import letterman

def main():
    # Conectando-se à planilha
    try:    
        SHEET_ID = SheetManager.sheetID
        sheet = SheetManager.sheet
        print("Planilha conectada com sucesso")

    except:
        print("ERRO CONECTANDO A PLANILHA")
        exit()

    while(1):

        # Descobrindo o último ID
        last_id = SheetManager.getLastID()

        print('Ingressos vendidos: '+last_id)
        key = int(input('1- Vender / 2- Atualizar dados / 3- Sair\n'))

        if key == 1:
            salesManager.sellTicket()
        elif key == 2:
            salesManager.updateInfos()
        else:
            exit()     

while(1):
    main()