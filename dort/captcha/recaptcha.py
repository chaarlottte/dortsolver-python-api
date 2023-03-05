from .task import TaskBase
from ..exceptions import InvalidKeyException

class ReCaptchaV3Task(TaskBase):
    def __init__(self, 
                apiKey: str, 
                publicKey: str,
                siteUrl: str, 
                callback: str = None,
                type: str = "invisible",
                proxy: str = None) -> None:
        super().__init__(apiKey, publicKey)
        self.siteUrl = siteUrl
        self.proxy = proxy
        self.callback = callback
        self.type = type

        if self.siteUrl.endswith("/"): self.siteUrl = self.siteUrl[:-1]
        pass

    def solve(self) -> str:
        body = {
          "api_key": self.apiKey,
          "site_key": self.publicKey,
          "site_url": self.siteUrl,
          "type": self.type
        }

        if self.proxy is not None:
            body.update({ "proxy_url": self.proxy })

        if self.callback is not None:
            body.update({ "callback": self.callback })

        resp = self.post(f"{self.baseUrl}/rc3", json=body)

        if resp.status_code == 200:
            if "game[token]" in resp.text:
                return resp.json().get("game[token]")
            else:
                return self.solve()
        else:
            raise InvalidKeyException("Your API key is invalid.")