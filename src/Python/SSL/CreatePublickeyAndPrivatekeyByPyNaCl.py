import nacl.utils
from nacl.public import PrivateKey, SealBox
#Create a couple key
private_key = PrivateKey.generate()
public_key = private_key.public_key
#Print the private key and public key
print(f"Public key: {public_key}")
print(f"Private key: {private_key}")
#Encrypt a message
message = b"Hello World!"
box = SealBox(public_key)
encrypted = box.encrypt(message)
print(f"Encrypted message: {encrypted}")
#Decrypt an encrypted message
box = SealBox(private_key)
decrypted = box.decrypt(encrypted)
print(f"Decrypted message: {decrypted}")