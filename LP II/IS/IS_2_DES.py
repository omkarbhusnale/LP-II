# DES Encryption Algorithm

# !pip install base32hex
# !pip install pyDes
# !pip install pycrypto

import base32hex
import hashlib
from Crypto.Cipher import DES
# import pyDes


password = "Password"
salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
key = password + salt
m = hashlib.md5(key)
key = m.digest()
(dk, iv) =(key[:8], key[8:])
crypter = DES.new(dk, DES.MODE_CBC, iv)

plain_text= "I see you"

print("The plain text is : ",plain_text)
plain_text += '\x00' * (8 - len(plain_text) % 8)

ciphertext = crypter.encrypt(plain_text)
encode_string= base32hex.b32encode(ciphertext)
print("The encoded string is : ",encode_string)

decrypted_string = crypter.decrypt(ciphertext)
print("The decrypted string is : ",decrypted_string)


# data = "DES Algorithm Implementation"
# k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
# d = k.encrypt(data)

# print ("Encrypted: {0}".format(d))
# print ("Decrypted: {0}".format(k.decrypt(d)))
