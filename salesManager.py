import qrcode
import SheetManager
import letterman

def sellTicket():
    # Email do cliente
    email = input('Inserir email: ')

    # Verificando se o email esta correto
    if input("O email está correto? "+email+"\n1-Sim / 2-Nao\n") == '2':
        print("Erro na venda. Favor tente novamente.")
        return

    # Criando o ID do cliente
    last_id = int(SheetManager.getLastID())
    id = str(last_id+1)

    # Gerando o QRCode e o salvando no computador
    code = qrcode.make("primeiroEmail-"+email+"-ID:"+id)
    code.show()
    code.save("QRCodes/qrcodeID"+id+".png")

    # Enviando o email com o QRCode
    letterman.sendMail(email, "qrcodeID"+id+".png", id)

    # Atualizando a planilha
    SheetManager.addCostumer(id, email)


    

