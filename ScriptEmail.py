import smtplib

print('Mandando Email...')

senha = ''
user = ''
contact = ['']

print('50% completo...')
server = smtplib.SMTP('smtp.office365.com', '587')
server.starttls()
server.login(user, senha)

de = user
para= contact
msg = """From: %s
To: %s
Subject: Email by Python

Hello World!""" % (de, ', '.join(para))

print('75% completo...')
server.sendmail(de, para, msg)
server.quit()

print('100% completo...')
print('Email enviado!')