from passlib.context import CryptContext

class PasswordSet():

    def __init__():
        pass

    def PassContext():
        self.pwd_context= CryptContext(
        schemes=["sha256_crypt"],
        default="sha256_crypt",
        sha256_crypt__min_rounds=30000
        )
        return self.pwd_context

    def encrypt_password(password):
        self.password=password
        self.pwd_context= self.PassContext()
        return pwd_context.encrypt(self.password)

    def check_encrypted_password(password,hashed):
        self.password=password
        self.hashed=hashed
        self.pwd_context= self.PassContext()
        return pwd_context.verify(self.password,self.hashed)

#context = PassContext()
#passhash = encrypt_password("MyPass")
#print (passhash)
#passcheck = check_encrypted_password("MyPass",passhash)
#print (passcheck)
