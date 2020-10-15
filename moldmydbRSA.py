# Generating a key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import sys
import base64

class HidePass():
    imhiding=''
    imviewing=''
    private_key=''
    public_key=''
    encrypted=''
    decrypted=''

    def __init__(self,text1,text2):
        self.message = text1
        self.message_bytes = self.message.encode('utf8')
        HidePass.imhiding = self.message_bytes


        self.base64_bytes = text2.encode('utf8')
        HidePass.imviewing = base64.b64decode(self.base64_bytes)

    def getFileUrl(self,filename,directory):
        if getattr(sys, 'frozen', False): # Running as compiled
            running_dir = sys._MEIPASS + "/" + directory + "/" #"/files/" # Same path name than pyinstaller option
        else:
            running_dir = "./" + directory + "/" # Path name when run with Python interpreter
        FileName = running_dir + filename #"moldmydb.png"
        return FileName

    def generatekeys(self):

        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        self.public_key = self.private_key.public_key()

        # Storing the keys

        self.pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        with open(self.getFileUrl("private_key.pem","keys"), 'wb') as f:
            f.write(self.pem)

        self.pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open(self.getFileUrl("public_key.pem","keys"), 'wb') as f:
            f.write(self.pem)


    def readingprivkey(self):
        # Reading the keys back in
        with open(self.getFileUrl("private_key.pem","keys"), "rb") as key_file:
            HidePass.private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    def readingpubkey(self):
        # Reading the key back in
        with open(self.getFileUrl("public_key.pem","keys"), "rb") as key_file:
            HidePass.public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    def hidepwd(self):
        # Encrypting
        HidePass.encrypted = HidePass.public_key.encrypt(
            HidePass.imhiding,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        self.base64_bytes = base64.b64encode(HidePass.encrypted)
        HidePass.encrypted=self.base64_bytes.decode('utf8')

    def unhidepwd(self):
        # Decrypting
        HidePass.decrypted = HidePass.private_key.decrypt(
            HidePass.imviewing,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        HidePass.decrypted = HidePass.decrypted.decode('utf8')

# Checking the results
#text = HidePass('1','')
#text.generatekeys()
#text.readingkeys()
#text.hidepwd()
#print("enc")
#print(text.encrypted)
#print (type(text.encrypted))

#text2=HidePass('',text.encrypted)
#text2.unhidepwd()
#print("dec")
#print(text2.decrypted)
#text.hidepwd()
#print(text.)
#pass.generatekeys()
