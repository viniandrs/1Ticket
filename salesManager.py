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
    
    # Pegando o telefone do cliente
    phone = input("Telefone: ")

    # Criando o ID do cliente
    last_id = int(SheetManager.getLastID())
    id = str(last_id+1)

    # Gerando o QRCode e o salvando no computador
    code = qrcode.make("primeiroEmail-"+email+\
                        "/phone-"+phone+"/ID:"+id)
    code.show()
    code.save("QRCodes/qrcodeID"+id+".png")

    # Enviando o email com o QRCode
    letterman.sendMail(email, "qrcodeID"+id+".png", id)

    # Atualizando a planilha
    SheetManager.addCostumer(id, email, phone)

def updateInfos():
    print("------- ATUALIZAR DADOS --------")
    id = input("ID: ")

    if SheetManager.readID(id) == 0:
        return

    key = input("Atualizar celular? 1- Sim / 2- Nao ")
    if key == '1':
        new_phone = input("Celular novo: ")
        SheetManager.updatePhone(id, new_phone)
    
    key = input("Atualizar email? 1- Sim / 2- Nao ")
    if key == '1':
        new_email = input("Email novo: ")
        
        if input("O email está correto? "+new_email+"\n1-Sim / 2-Nao\n") == '2':
            print("Erro na venda. Favor tente novamente.")
            return
            
        SheetManager.updateEmail(id, new_email)

        #Reenviando o email
        key = input("Reenviar email? 1- Sim / 2- Não ")
        if key == '1':
            letterman.sendMail(new_email, "qrcodeID"+id+".png", id)
    

