from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def decryptFile(inputFile, outputFile, key):
    cipher = PKCS1_OAEP.new(key)

    with open(inputFile, 'rb') as i, open(outputFile, 'wb') as j:
        while True:
            chunk = i.read(256)
            if len(chunk) == 0:
                break
            decrypted_chunk = cipher.decrypt(chunk)
            j.write(decrypted_chunk)

# Load private key
private_key_filename = input("Enter the private key file name: ")
private_key = RSA.import_key(open(private_key_filename, 'rb').read())

# Decrypt the encrypted file with private key
encrypted_file = input("Enter the encrypted file name: ")
decryptedFile = input("enter output filename: ") + ".dec.li8ght"
decryptFile(encrypted_file, decryptedFile, private_key)
print("File decrypted with private key.")
print("Encrypted Filename :" + decryptedFile)
