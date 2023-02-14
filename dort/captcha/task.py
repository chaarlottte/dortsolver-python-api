import requests

class TaskBase():
    def __init__(self, apiKey: str, publicKey: str) -> None:
        self.apiKey = apiKey
        self.publicKey = publicKey
        self.baseUrl = "https://api.dort.shop/captcha/solve"
        self.session = requests.Session()
        pass

    def solve(self) -> str:
        return "TO IMPL"
  
    def get(self, url: str, *args, **kwargs) -> requests.Response:
        return self.session.get(url, *args, **kwargs)

    def post(self, url: str, *args, **kwargs) -> requests.Response:
        return self.session.post(url, *args, **kwargs)