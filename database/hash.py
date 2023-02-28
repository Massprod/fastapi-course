from passlib.context import CryptContext


class Hash(CryptContext):
    def __init__(self):
        super().__init__(schemes="bcrypt", deprecated="auto")

    def bcrypt_pass(self, password: str):
        return self.hash(password)

    def verify_pass(self, hashed_password, plain_password):
        return self.verify(plain_password, hashed_password)
