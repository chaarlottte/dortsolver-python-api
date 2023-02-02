# DortSolver Python API
(absolute insanity)

Using [dort](https://github.com/dort-dev)'s API, which you can purchase at [discord.gg/funcaptcha](https://discord.gg/funcaptcha).

Not going to be hosted on pip for now, maybe later when I have more time lol.



## Quick, bad documentation

### Installation
Drag the `dort` folder into your project. The only requirement is the `requests` module, which you can install with `pip install requests`.

### Simple example
```python
import dort

solver = dort.Solver(
    apiKey="your-api-key", # Your DortSolver API key.
    publicKey="B7D8911C-5CC8-A9A3-35B0-554ACEE604DA", # The Funcaptcha public key of the website you wish to solve on.
    siteUrl="https://iframe.arkoselabs.com", # The URL of the site you are wishing to solve on (e.g. https://iframe.arkoselabs.com for outlook)
    apiUrl="https://client-api.arkoselabs.com", # Optional. Defaults to https://client-api.arkoselabs.com/.
    blob="blob", # Optional. Not needed for Outlook, or any other site I've tried besides ROBLOX.
    proxy="socks5://user:pass@host:port"
)

# Returns the game token as a str.
# `retry` instructs the solver whether or not to immediately retry on a failed solve attempt.
token = solver.solve(retry=True)

# Now do whatever you want with the captcha token :)
print(token)
```

### Outlook Example
```python
outlookSolver = dort.OutlookSolver(
    apiKey="your-api-key",
    proxy="socks5://user:pass@host:port" # Optional. Dort's proxies work best for Outlook, but ig you can use your own?
)

# And, of course, simply get the token as such:
outlookToken = outlookSolver.solve()
```

### ROBLOX Example
```python
from dort.builtin import RobloxCaptchaType
robloxSolver = dort.RobloxSolver(
    apiKey="your-api-key",
    # Roblox has a different public key (that they change weekly or so) for each task, this will automatically fetch them for you!
    captchaType=RobloxCaptchaType.SIGNUP,
    blob="blob", # 99% sure that blob is required for all, but it might not be for some.
    proxy="socks5://user:pass@host:port" # Optional, of course!
)

# And, of course, simply get the token as such:
robloxToken = robloxSolver.solve()
```
