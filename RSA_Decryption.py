import random
import os
import pickle


def RSADecryption(filename):
          
              
    
    
    def decrypt(pk, ciphertext):
       
        key, n = pk
        
        plain = [chr((char ** key) % n) for char in ciphertext]
        
        return ''.join(plain)
    
    
    
    def decrypt_file(file_name):
        with open('encrypted files/'+file_name,'rb') as fo:
                ciphertext=fo.read()
            
        datas2=pickle.loads(ciphertext)
       
        with open('encrypted files/keys.txt','rb') as foo:
                keyy=foo.read()
    
        key=pickle.loads(keyy)
        print key
        dec=decrypt(key,datas2)
        directory1="received_files"
        if not os.path.exists(directory1):
                os.makedirs(directory1)
        directory1=directory1+'/'
        with open(directory1+file_name[:-4], 'wb') as fo:
                fo.write(dec)
    
    
    decrypt_file(filename)
