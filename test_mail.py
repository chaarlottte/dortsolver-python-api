"""import dort

mail = dort.DortMail("apiKey")
print(mail.getTypes())
print(mail.getBalance())
dortMail = mail.purchaseMails(type=1, amount=1)[0]
x: MailMessage
for x in dortMail.getMailbox():
    print(x.subject)
"""
import dort
from imap_tools import MailMessage
address = dort.DortMailAddress("stevemolon75353@outlook.com", "L3yf$DortGen")

x: MailMessage
for x in address.getMailbox():
    print(x.subject)