from passlib.context import CryptContext

def PassContext():
    pwd_context= CryptContext(
    schemes=["sha256_crypt"],
    default="sha256_crypt",
    sha256_crypt__min_rounds=30000
    )
    return pwd_context

def encrypt_password(password):
    pwd_context= PassContext()
    return pwd_context.encrypt(password)

def check_encrypted_password(password,hashed):
    pwd_context= PassContext()
    return pwd_context.verify(password,hashed)

#context = PassContext()
#passhash = encrypt_password("MyPass")
#print (passhash)
#passcheck = check_encrypted_password("MyPass",passhash)
#print (passcheck)
