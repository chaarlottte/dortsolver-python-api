from dort.mail import DortMail
from imap_tools import MailMessage

mail = DortMail("apiKey")
print(mail.getTypes())
print(mail.getBalance())
dortMail = mail.purchaseMails(type=1, amount=1)[0]
x: MailMessage
for x in dortMail.getMailbox():
    print(x.subject)