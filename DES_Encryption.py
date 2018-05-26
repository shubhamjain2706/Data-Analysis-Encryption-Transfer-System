from pyDes import *
import os
from binascii import unhexlify as unhex


def DESEncryption(filename):

    def _example_triple_des_(file_name):
        k1 = des(unhex("133457799BBCDFF1"))
        k2 = des(unhex("1122334455667788"))
        k3 = des(unhex("77661100DD223311"))
        with open(file_name, 'rb') as fo:
            d = fo.read()
        

        e1 = k1.encrypt(d,padmode=PAD_PKCS5)
        e2 = k2.decrypt(e1,padmode=PAD_PKCS5)
        e3 = k3.encrypt(e2,padmode=PAD_PKCS5)
        

    
        directory1="encrypted files"
        if not os.path.exists(directory1):
            os.makedirs(directory1)
        directory1=directory1+'/'
        with open(directory1+file_name+'.enc', 'wb') as fo:
            fo.write(e3)
    

    directory,file_name=os.path.split(filename)
    _example_triple_des_(file_name)
    return file_name+".enc"


