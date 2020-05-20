from scrapy.mail import MailSender

mailer = MailSender()

# or instantiate it passing a scrapy settings object
mailer = MailSender.from_settings(settings)

# how to use it to send an e-mail
mailer.send(to=["someone@example.com"], subject="Some subject", body="Some body", cc=["another@example.com"])
