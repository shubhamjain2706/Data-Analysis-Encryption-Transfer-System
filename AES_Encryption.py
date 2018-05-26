#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
import os

def AESEncryption(filename):
	def pad(s):
		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	def encrypt(message, key, key_size=256):
		message = pad(message)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CBC, iv)
		return iv + cipher.encrypt(message)


	def encrypt_file(file_name, key):
		with open(filename, 'rb') as fo:
			plaintext = fo.read()
		enc = encrypt(plaintext, key)
		directory1="encrypted files"
                if not os.path.exists(directory1):
                        os.makedirs(directory1)
                directory1=directory1+'/'
		with open(directory1+file_name+'.enc', 'wb') as fo:
			fo.write(enc)

	

	key ='0123456789abcdef'
        directory,file_name=os.path.split(filename)
	encrypt_file(file_name, key)

        return file_name+".enc"
