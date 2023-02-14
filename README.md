# DortSolver Python API
(absolute insanity)

Using [dort](https://github.com/discord-trollering)'s API, which you can purchase at [discord.gg/funcaptcha](https://discord.gg/funcaptcha).

Not going to be hosted on pip for now, maybe later when I have more time lol.

Now also featuring Dort's tempmail services! You can purchase it at [discord.gg/emails](https://discord.gg/emails).

## Quick, bad documentation

### Installation
Drag the `dort` folder into your project. The only requirement are the `requests` module and the `imap-tools` module, both of which you can install as such:
```sh
$ pip install requests imap-tools
```

### Solve FunCaptcha
```python
from dort.captcha import FuncaptchaTask


funcapSolver = FuncaptchaTask(
    apiKey="your api key", # Your DortSolver API key.
    publicKey="B7D8911C-5CC8-A9A3-35B0-554ACEE604DA", # The Funcaptcha public key of the website you wish to solve on.
    siteUrl="https://iframe.arkoselabs.com", # The URL of the site you are wishing to solve on (e.g. https://iframe.arkoselabs.com for outlook)
    apiUrl="https://client-api.arkoselabs.com", # Optional. Defaults to https://client-api.arkoselabs.com/.
    blob="blob", # Optional. Not needed for Outlook, or any other site I've tried besides ROBLOX.
    proxy="socks5://user:pass@host:port"
)

print(funcapSolver.solve())
```

### Solve HCaptcha
```python
from dort.captcha import HCaptchaTask

hcapSolver = HCaptchaTask(
    apiKey="your api key", # Your DortSolver API key.
    publicKey="a5f74b19-9e45-40e0-b45d-47ff91b7a6c2",  # The HCaptcha public key of the website you wish to solve on.
    siteUrl="https://accounts.hcaptcha.com/demo/", # The URL of the site you are wishing to solve on 
    proxy="socks5://user:pass@host:port" # (Optional) Your proxy URL. Formatted as protocol://user:pass@host:port
)

print(hcapSolver.solve())
```

### DortGen Email Example
```python
from dort.mail import DortMail
from imap_tools import MailMessage

mail = DortMail("apiKey") # Replace with your API key.

print(mail.getTypes()) # Print out the currently available email types.
print(mail.getBalance()) # Print out your current balance.

dortMail = mail.purchaseMails(type=1, amount=1)[0] # Returns an array of type DortMailAddress.

x: MailMessage # This is included with the imap_tools library, used for fetching emails.
for x in dortMail.getMailbox(): # Get the entire mailbox
    print(x.subject) # Print out the subject of the message.

x: MailMessage
for x in address.getEmailsFromSender("noreply@discord.com"): # This will do the same as above, but only show emails from a specific address.
    print(x.subject)
```

You can also simply login to any outlook/hotmail email address and check it with this API, but it's essentially wrapping a pre-existing IMAP library, so it may be in your best interest to instead just use that. You can find said IMAP library [here](https://pypi.org/project/imap-tools/).

```python
from dort.mail import DortMailAddress
from imap_tools import MailMessage

address = DortMailAddress("stevemolon75353@outlook.com", "L3yf$DortGen") # Login to account with email and password

x: MailMessage # This is included with the imap_tools library, used for fetching emails.
for x in dortMail.getMailbox(): # Get the entire mailbox
    print(x.subject) # Print out the subject of the message.
```