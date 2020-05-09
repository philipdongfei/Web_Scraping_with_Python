import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'philip.dong@outlook.com' #'christmas_alerts@pythonscraping.com'
    msg['To'] = 'philip.dong@hotmail.com' #ryan@pythonscraping.com

    try:
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
        print('Successfully send msg')
    except SMTPException:
        print('Error: unable to send msg')

if __name__ == '__main__':
    bs = BeautifulSoup(urlopen('https://isitchristmas.com/'), 'html.parser')
    while (bs.find('a', {'id':'answer'}).attrs['title'] == 'NO'):
        print('It is not Christmas yet.')
        time.sleep(3600)
        bs = BeautifulSoup(urlopen('https://isitchristmas.com/'), 'html.parser')
    sendMail('It\'s Christmas!',
             'According to http://itischristmas.com, it is Christmas!')


