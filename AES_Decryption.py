#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
import os

def AESDecryption(filename):
	def pad(s):
		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	
	def decrypt(ciphertext, key):
		iv = ciphertext[:AES.block_size]
		cipher = AES.new(key, AES.MODE_CBC, iv)
		plaintext = cipher.decrypt(ciphertext[AES.block_size:])
		return plaintext.rstrip(b"\0")

	

	def decrypt_file(file_name, key):
		with open(filename, 'rb') as fo:
			ciphertext = fo.read()
		dec = decrypt(ciphertext, key)
		with open(filename[:-4], 'wb') as fo:
			fo.write(dec)


	key ='0123456789abcdef'
        directory,file_name=os.path.split(filename)
	
	decrypt_file(file_name, key)
     
