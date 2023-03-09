from dort.captcha import HCaptchaTask, FuncaptchaTask, ReCaptchaV3Task, HCaptchaEnterpriseTask
import os

funcapSolver = FuncaptchaTask(
    apiKey=os.getenv("api_key"), # Your DortSolver API key.
    publicKey="B7D8911C-5CC8-A9A3-35B0-554ACEE604DA", # The Funcaptcha public key of the website you wish to solve on.
    siteUrl="https://iframe.arkoselabs.com", # The URL of the site you are wishing to solve on (e.g. https://iframe.arkoselabs.com for outlook)
    apiUrl="https://client-api.arkoselabs.com", # Optional. Defaults to https://client-api.arkoselabs.com/.
    blob="blob", # Optional. Not needed for Outlook, or any other site I've tried besides ROBLOX.
    #proxy="socks5://user:pass@host:port"
)
print(funcapSolver.solve())

hcapSolver = HCaptchaTask(
    apiKey=os.getenv("api_key"), # Your DortSolver API key.
    publicKey="a5f74b19-9e45-40e0-b45d-47ff91b7a6c2",  # The HCaptcha public key of the website you wish to solve on.
    siteUrl="https://accounts.hcaptcha.com/demo/", # The URL of the site you are wishing to solve on 
    #proxy="socks5://user:pass@host:port" # (Optional) Your proxy URL. Formatted as protocol://user:pass@host:port
)
print(hcapSolver.solve())

recapSolver = ReCaptchaV3Task(
    apiKey=os.getenv("api_key"),
    publicKey="6LdyC2cUAAAAACGuDKpXeDorzUDWXmdqeg-xy696", 
    siteUrl="https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php",
    callback="https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php?token="
)
print(recapSolver.solve())

hcapEnterpriseSolver = HCaptchaEnterpriseTask(
    apiKey=os.getenv("api_key"), # Your DortSolver API key.
    publicKey="4c672d35-0701-42b2-88c3-78380b0db560",  # The HCaptcha public key of the website you wish to solve on.
    siteUrl="https://discord.com", # The URL of the site you are wishing to solve on 
    #proxy="socks5://user:pass@host:port" # (Optional) Your proxy URL. Formatted as protocol://user:pass@host:port
)
print(hcapEnterpriseSolver.solve())