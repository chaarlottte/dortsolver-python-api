class UnsupportedProxyException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class SolverErrorException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidKeyException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)