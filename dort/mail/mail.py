from requests import Response
from ..exceptions import InvalidKeyException
from imap_tools import MailBox, MailMessage, AND
import requests, json

class DortMailAddress():
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password
        pass

    def getMailbox(self):
        messages = []
        with MailBox("outlook.office365.com").login(self.email, self.password) as mailbox: 
            for msg in mailbox.fetch():
                messages.append(msg)
        return messages
    
    def getEmailsFromSender(self, sender: str):
        messages = []
        with MailBox("outlook.office365.com").login(self.email, self.password) as mailbox: 
            for msg in mailbox.fetch(AND(from_=sender)):
                messages.append(msg)
        return messages

    def log(self):
        print(self.email, self.password)

class DortMail():
    def __init__(self, key: str) -> None:
        self.key = key
        pass

    def purchaseMails(self, type: int, amount: int) :
        data: dict = {
            "key": self.key,
            "type": type,
            "amount": amount
        }
        resp = requests.get("https://api.dort.shop/mail/purchase", data)

        if resp.status_code == 200:
            accounts = []

            for acc in resp.json()["accounts"]:
                accounts.append(DortMailAddress(email=acc["email"], password=acc["password"]))
            return accounts
        else:
            raise InvalidKeyException("Your API key is invalid.")

    def getBalance(self) -> float:
        data: dict = {
            "key": self.key
        }
        resp: dict = requests.get("https://api.dort.shop/mail/balance", data)

        if resp.status_code == 200:
            return resp.json()["balance"]
        else:
            raise InvalidKeyException("Your API key is invalid.")

    def getTypes(self) -> dict:
        resp: dict = requests.get("https://api.dort.shop/mail/types").json()

        typeArray = []
        typeDict = { }

        for x in resp.keys():
            if x is not None:
                friendlyType: str = x.split(" (")[0]
                code: int = resp[x]["code"]
                price: float = resp[x]["price"]
                typeArray.append({ "name": friendlyType, "code": code, "price": price })

        typeDict.update({ "types": typeArray })
        return typeDict