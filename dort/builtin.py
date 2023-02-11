import requests
from .exceptions import *
from .solver import *
from enum import Enum

class RobloxCaptchaType(Enum):
    SIGNUP = "ACTION_TYPE_WEB_SIGNUP"
    LOGIN = "ACTION_TYPE_WEB_LOGIN"
    RESET_PASSWORD = "ACTION_TYPE_WEB_RESET_PASSWORD"
    ASSET_COMMENT = "ACTION_TYPE_ASSET_COMMENT"
    ASSET_UPLOAD = "ACTION_TYPE_CLOTHING_ASSET_UPLOAD"
    FOLLOW_USER = "ACTION_TYPE_FOLLOW_USER"
    GENERIC = "ACTION_TYPE_GENERIC_CHALLENGE"
    JOIN_GROUP = "ACTION_TYPE_GROUP_JOIN"
    WALL_POST = "ACTION_TYPE_GROUP_WALL_POST"
    SUPPORT_REQUEST = "ACTION_TYPE_SUPPORT_REQUEST"
    REDEEM_GIFTCARD = "ACTION_TYPE_WEB_GAMECARD_REDEMPTION"

class RobloxSolver(Solver):
    def __init__(self, apiKey: str, captchaType: RobloxCaptchaType, blob: str = None, proxy: str = None) -> None:
        self.captchaType = captchaType

        pKey = self.getRobloxPublicKey()
        super().__init__(apiKey, pKey, "https://roblox.com", blob, "https://roblox-api.arkoselabs.com/", proxy)

    def getRobloxPublicKey(self) -> str:
        allKeys = requests.get("https://apis.roblox.com/captcha/v1/metadata").json()["funCaptchaPublicKeys"]
        return allKeys[self.captchaType.value]

class OutlookSolver(Solver):
    def __init__(self, apiKey: str, proxy: str = None, publicKey: str = "B7D8911C-5CC8-A9A3-35B0-554ACEE604DA") -> None:
        super().__init__(
            apiKey, 
            publicKey, 
            "https://iframe.arkoselabs.com", 
            None, 
            "https://client-api.arkoselabs.com", 
            proxy
        )
