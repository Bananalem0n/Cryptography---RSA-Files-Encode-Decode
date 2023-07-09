from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def generateKeypair():
    key = RSA.generate(2048)
    return key

def saveKey(key, filename):
    with open(filename, 'wb') as file:
        file.write(key.export_key('PEM'))

def loadKey(filename, passphrase=None):
    with open(filename, 'rb') as file:
        key_data = file.read()
        return RSA.import_key(key_data, passphrase=passphrase)

def encodeFile(inputFile, outputFile, key):
    cipher = PKCS1_OAEP.new(key)

    with open(inputFile, 'rb') as i, open(outputFile, 'wb') as j:
        while True:
            chunk = i.read(256)
            if len(chunk) == 0:
                break
            encrypted_chunk = cipher.encrypt(chunk)
            j.write(encrypted_chunk)

# Generate key pair
keyPair = generateKeypair()

# Save public and private keys
publicKeyFile = input("Enter the public key file name: ")
privateKeyFile = input("Enter the private key file name: ")

if os.path.exists(publicKeyFile) or os.path.exists(privateKeyFile):
    print("Error: Key file already exists.")
    exit(1)

saveKey(keyPair.publickey(), publicKeyFile)
saveKey(keyPair, privateKeyFile)
print("Keys saved successfully.")

# Load keys
public_key = loadKey(publicKeyFile)
private_key = loadKey(privateKeyFile)

# Encrypt file with public key
inputFile = input("Enter the input file name: ")
encrypted_file = input("enter output filename: ") + ".enc.li8ght"
encodeFile(inputFile, encrypted_file, public_key)
print("File encrypted with public key.")
print("Encrypted Filename :" + encrypted_file)

