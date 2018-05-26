import random
import os
import pickle


def RSAEncryption(filename):

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def multiplicative_inverse(e, phi):
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        temp_phi = phi
    
        while e > 0:
            temp1 = temp_phi/e
            temp2 = temp_phi - temp1 * e
            temp_phi = e
            e = temp2
        
            x = x2- temp1* x1
            y = d - temp1 * y1
        
            x2 = x1
            x1 = x
            d = y1
            y1 = y
    
        if temp_phi == 1:
            return d + phi

    
    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for n in xrange(3, int(num**0.5)+2, 2):
            if num % n == 0:
                return False
        return True

    def generate_keypair(p, q):
        if not (is_prime(p) and is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')
        
        n = p * q

        
        phi = (p-1) * (q-1)

        
        e = random.randrange(1, phi)

       
        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)
        
        
        d = multiplicative_inverse(e, phi)
    
        
        return ((e, n), (d, n))




    def encrypt(pk, plaintext):
       
        key, n = pk
       
        cipher = [(ord(char) ** key) % n for char in plaintext]
      
        return cipher
    
    def encrypt_file(file_name, key, key2):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = encrypt(key,plaintext)
        datas1=pickle.dumps(enc)
        datas2=pickle.dumps(key2)
                
        directory1="encrypted files"
        if not os.path.exists(directory1):
                       os.makedirs(directory1)
        directory1=directory1+'/'
        with open(directory1+file_name+'.enc', 'wb') as fo:
                        fo.write(datas1)
        with open(directory1+'keys.txt','wb') as foo:
                        foo.write(datas2)




                
                
                
    directory,file_name=os.path.split(filename)
    p = 17
    q = 19
    print "Generating your public/private keypairs now . . ."
    public, private = generate_keypair(p, q)
    print "Your public key is ", public ," and your private key is ", private
    encrypt_file(file_name,private,public) 
    return file_name+".enc"
