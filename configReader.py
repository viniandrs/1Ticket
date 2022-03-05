with open('config.txt') as file:
    lines = file.readlines()

    # Obtendo o email do vendedor
    email_words = lines[0].split()
    email = email_words[-1]

    # Obtendo a senha do vendedor
    password_words = lines[1].split()
    password = password_words[-1]
    
    # Obtendo o ID do googlesheet
    sheetID_words = lines[2].split()
    sheetID = sheetID_words[-1]

    # Obtendo o assunto padrao do email
    defaultSubject_words = lines[3].split()
    subject = ""
    for i in range(3, len(defaultSubject_words)):
        subject = subject + defaultSubject_words[i] + " "

    # Obtendo o texto padrao do email
    body = ""
    for i in range(6, len(lines) - 1):
        body = body + lines[i]
