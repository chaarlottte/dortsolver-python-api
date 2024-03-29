from .task import TaskBase
from ..exceptions import InvalidKeyException, SolverErrorException
from typing import Literal

class FuncaptchaTask(TaskBase):
    def __init__(self, 
                apiKey: str, 
                publicKey: str,
                siteUrl: str, 
                blob: str = None, 
                apiUrl: str = "https://client-api.arkoselabs.com",
                proxy: str = None,
                userAgent: str = None,
                type: Literal["audio-test", "image-test", "image-prod-test"] = "audio-test") -> None:
        super().__init__(apiKey, publicKey)
        self.blob = blob
        self.apiUrl = apiUrl
        self.siteUrl = siteUrl
        self.proxy = proxy
        self.userAgent = userAgent
        self.type = type

        if self.siteUrl.endswith("/"): self.siteUrl = self.siteUrl[:-1]
        if self.apiUrl.endswith("/"): self.apiUrl = self.apiUrl[:-1]
        if userAgent is not None:
            self.session.headers.update({
                "User-Agent": self.userAgent
            })
        pass

    def solve(self) -> str:
        body = {
          "type": self.type,
          "api_key": self.apiKey,
          "site_key": self.publicKey,
          "site_url": self.siteUrl,
          "surl": self.apiUrl,
        }

        if self.userAgent is not None:
            body.update({ "user_agent": self.userAgent })

        if self.proxy is not None:
            body.update({ "proxy_url": self.proxy })

        if self.blob is not None:
            body.update({ "data": { "blob": self.blob } })

        resp = self.post(f"{self.baseUrl}/fc", json=body)

        try:
            if resp.json().get("solver[error]") is not None:
                error = resp.json().get("solver[error]")
                if error == "no user found for provided api key.":
                    raise InvalidKeyException("Your API key is invalid.")
                else:
                    raise SolverErrorException(error)
            else:
                if resp.status_code == 200:
                    if "game[token]" in resp.text:
                        return resp.json().get("game[token]")
                    else:
                        return self.solve()
        except Exception as e:
            raise SolverErrorException(e)