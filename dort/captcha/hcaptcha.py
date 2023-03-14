from .task import TaskBase
from ..exceptions import InvalidKeyException, SolverErrorException

class HCaptchaTask(TaskBase):
    def __init__(self, 
                apiKey: str, 
                publicKey: str,
                siteUrl: str, 
                proxy: str = None,
                userAgent: str = None, 
                data: str = None) -> None:
        super().__init__(apiKey, publicKey)
        self.siteUrl = siteUrl
        self.proxy = proxy
        self.userAgent = userAgent
        self.data = data

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
        
        if self.userAgent is not None:
            body.update({ "agent": self.userAgent })

        if self.data is not None:
            body.update({ "rqdata": self.data })

        resp = self.post(f"{self.baseUrl}/hc", json=body)

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

class HCaptchaEnterpriseTask(TaskBase):
    def __init__(self, 
                apiKey: str, 
                publicKey: str,
                siteUrl: str, 
                proxy: str = None,
                userAgent: str = None, 
                data: str = None) -> None:
        super().__init__(apiKey, publicKey)
        self.siteUrl = siteUrl
        self.proxy = proxy
        self.userAgent = userAgent
        self.data = data

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
        
        if self.userAgent is not None:
            body.update({ "agent": self.userAgent })

        if self.data is not None:
            body.update({ "rqdata": self.data })

        resp = self.post(f"{self.baseUrl}/hc-enterprise", json=body)


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