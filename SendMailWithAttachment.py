import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

 

# Setting Variables
FILE_NAME = ".xlsx" # It is recommended to put the file in the work path of the code
FROM = ''
TO = ''
SUBJECT = ''
EMAIL_BODY = ''

 

# Run the script
SourcePathName  = os.path.join(os.getcwd(), FILE_NAME)
msg = MIMEMultipart()
msg['From'] = FROM
msg['To'] = TO
msg['Subject'] = SUBJECT
body = EMAIL_BODY

 

msg.attach(MIMEText(body, 'plain'))
attachment = open(SourcePathName, 'rb')
part = MIMEBase('application', "octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % FILE_NAME)
msg.attach(part)
server = smtplib.SMTP()
server.ehlo()
server.starttls()
server.ehlo()
server.send_message(msg)
server.quit()

print('Email with attachment sent successfully!')
