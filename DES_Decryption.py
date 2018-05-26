from pyDes import *
import os

def DESDecryption(filename):
    
    
    
    
        
        from binascii import unhexlify as unhex

    
  
        k1 = des(unhex("133457799BBCDFF1"))
        k2 = des(unhex("1122334455667788"))
        k3 = des(unhex("77661100DD223311"))
    
     
        directory1="encrypted files"
        if not os.path.exists(directory1):
            os.makedirs(directory1)
        directory1=directory1+'/'
        with open(directory1+filename, 'rb') as fo:
            plaintext = fo.read()
        d3 = k3.decrypt(plaintext,padmode=PAD_PKCS5)
        d2 = k2.encrypt(d3,padmode=PAD_PKCS5)
        d1 = k1.decrypt(d2,padmode=PAD_PKCS5)
        
    
        directory2="received_files"
        if not os.path.exists(directory2):
            os.makedirs(directory2)
        directory2=directory2+'/'
        with open(directory2+filename[:-4], 'wb') as fo:
            fo.write(d1)

       


    
        
