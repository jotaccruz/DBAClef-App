from cryptography.fernet import Fernet

def newkey():
    key = Fernet.generate_key()
    return key

def encryptPass(Pass,key):
    cipher_suite= Fernet(key)
    ciphered_text=cipher_suite.encrypt(bytes(Pass,"utf-8")) #required to be bytes
    return ciphered_text

def decryptPass(Pass,key):
    cipher_suite= Fernet(key)
    unciphered_text=(cipher_suite.decrypt(Pass))
    #print (unciphered_text)
    plain_text_encryptedpassword= bytes(unciphered_text).decode("utf-8") #convert to StringVar
    return plain_text_encryptedpassword

key = newkey()
print (type(key))
Pass=encryptPass("MyPass",key)
print (Pass)
Pass=decryptPass(Pass,key)
print (Pass)
