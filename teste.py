# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252


# import urllib2
# import json

# data = urllib2.urlopen('http://api.postmon.com.br/v1/cep/29055020')

# if data.code != 200:
# 	print('Ops, deu errado!')

# j = json.loads(data.read())

# print(json.dumps(j))

# t = """
# +--------------------------------------+
# |                                      |
# |            FRETE RAPIDO              |
# |                                      |
# +--------------------------------------+
# |               ATENCAO                |
# | O saldo do Jelastic esta em R$ %.2f |
# | Cuidado para nao esgotar!            |
# | Frete Rapido precisa deste servico   |
# | para funcionar.                      |
# |                                      |
# +--------------------------------------+
# """

# print(t % 65.86)
# 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = '74cbcd0890472c'
password = 'a7a5bf6583215e'
sender = 'naoresponda@freterapido.com'
receiver = 'alves.david@outlook.com'

cc = 'web.alisson@freterapido.com, ti.leonardo@freterapido.com'

msg = MIMEMultipart('alternative')

# sender == the sender's email address
# receiver == the recipient's email address
msg['Subject'] = 'Saldo do Jelastic'
msg['From'] = sender
msg['To'] = receiver
msg['Cc'] = cc

html = open('index.html', 'r')
content = MIMEText(html.read() % 57.60, 'html')
html.close()

msg.attach(content)

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.mailtrap.io', 2525)
s.login(user, password)
s.sendmail(sender, receiver, msg.as_string())
s.quit()
print('Sucesso!')