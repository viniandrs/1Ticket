from distutils.command.config import config
import smtplib
import imghdr
from email.message import EmailMessage

import configReader

def sendMail(recipient, qrcode, id):

    # Obtendo informacoes do email a partir do arquivo config.txt
    # e gerando o email
    email_id = configReader.email
    email_pass = configReader.password
    msg = EmailMessage()
    msg['Subject'] = configReader.subject
    msg['From'] = email_id
    msg['To'] = recipient
    msg.set_content(configReader.body.format(id))

    # Adicionando o QRCode como anexo
    with open("QRCodes/"+qrcode, "rb") as img:
        file_data = img.read()
        file_type = imghdr.what(img.name)
        file_name = img.name
        msg.add_attachment(file_data, 
                            maintype = 'image', 
                            subtype = file_type, 
                            filename = file_name)

    # Enviando o email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)
    
    print("\nQRCode enviado por email!")
