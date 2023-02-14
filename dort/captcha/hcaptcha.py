from .task import TaskBase
from ..exceptions import InvalidKeyException

class HCaptchaTask(TaskBase):
    def __init__(self, 
                 apiKey: str, 
                 publicKey: str,
                 siteUrl: str, 
                 proxy: str = None,) -> None:
        super().__init__(apiKey, publicKey)
        self.siteUrl = siteUrl
        self.proxy = proxy

        if self.siteUrl.endswith("/"): self.siteUrl = self.siteUrl[:-1]
        pass

    def solve(self) -> str:
        body = {
          "api_key": self.apiKey,
          "site_key": self.publicKey,
          "site_url": self.siteUrl
        }

        if self.proxy is not None:
            body.update({ "proxy_url": self.proxy })

        resp = self.post(f"{self.baseUrl}/hc", json=body)

        if resp.status_code == 200:
            if "game[token]" in resp.text:
                return resp.json().get("game[token]")
            else:
                return self.solve()
        else:
            raise InvalidKeyException("Your API key is invalid.")