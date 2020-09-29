from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib
import os

print('Mandando Email...')
msg = MIMEMultipart()

print('50% completo...')

user = ''
password = ''
msg['From'] = ''
msg['To'] = ''
msg['Subject'] = 'Email by Python'
body = "Hello World!"
msg.attach(MIMEText(body, 'plain'))

filename = ''
attachment = open(filename, 'rb')
part = MIMEBase('application', "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="teste.xlsx"')
encoders.encode_base64(part)
msg.attach(part)

server = smtplib.SMTP('smtp.office365.com', '587')
server.starttls()
server.login(user, password)

print('75% completo...')
server.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
server.quit()

print('100% completo...')
print('Email enviado!')