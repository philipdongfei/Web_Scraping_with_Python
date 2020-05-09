import smtplib
from email.mime.text import MIMEText

msg = MIMEText('The body of the email is here')

msg['Subject'] = 'An Email Alert'
msg['From'] = 'philip.dong@outlook.com'
msg['To'] = 'philip.dong@hotmail.com'

try:
    #s = smtplib.SMTP('smtp-mail.outlook.com', 587)
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    print('Successfully send msg')
except SMTPException:
    print('Error: unable to send msg')



