import requests
from .exceptions import *

class Solver():
    def __init__(self, 
                apiKey: str, 
                publicKey: str, 
                siteUrl: str, 
                blob: str = None, 
                apiUrl: str = "https://client-api.arkoselabs.com",
                proxy: str = None) -> None:
        self.apiKey = apiKey
        self.publicKey = publicKey
        self.blob = blob
        self.apiUrl = apiUrl
        self.siteUrl = siteUrl
        self.proxy = proxy

        if self.siteUrl.endswith("/"): self.siteUrl = self.siteUrl[:-1]
        if self.apiUrl.endswith("/"): self.apiUrl = self.apiUrl[:-1]
        pass

    def solve(self, retry: bool = False) -> str:
        body = {
            "api_key": self.apiKey,
            "site_key": self.publicKey,
            "surl": self.apiUrl,
            "site_url": self.siteUrl
        }

        if self.blob is not None:
            body.update({"data": { "blob": self.blob }})

        if self.proxy is not None:
            body.update({ "proxy_url": self.proxy })

        try:
            resp = requests.post("https://captcha-api.slave-auction.shop/solve/fc", json=body)
            if "error" in resp.json():
                if retry:
                    return self.solve(retry=retry)
                else: raise SolverErrorException(f"Solver API returned error: {resp.json()['error']}")
            return resp.json()["game[token]"]
        except Exception as e:
            print(e)
            if retry:
                return self.solve(retry=retry)
            else: raise SolverErrorException(f"Solver API returned error: {resp.json()['error']}")