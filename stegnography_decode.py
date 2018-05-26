
import os
from PIL import Image
import binascii

def str2bin(message):
    binary=bin(int(binascii.hexlify(message),16))
    return binary[2:]

def bin2str(binary):
    message=binascii.unhexlify('%x'%(int('0b'+binary,2)))
    return message



def decode(filename):
    img1=Image.open(filename)
    pixels = img1.load() # create the pixels map
    x=""
    for i in range(img1.size[0]):    # for every pixels:
        for j in range(img1.size[1]):
            #print pixels[i,j],"\t",bin(pixels[i,j][0])[-1],"\t",bin(pixels[i,j][1])[-1],"\t",bin(pixels[i,j][2])[-1]
            x+=bin(pixels[i,j][0])[-1]
            if x.find("1111111111111110")>=0:
                break
            x+=bin(pixels[i,j][1])[-1]
            if x.find("1111111111111110")>=0:
                break
            x+=bin(pixels[i,j][2])[-1]
            if x.find("1111111111111110")>=0:
                break
        if x.find("1111111111111110")>=0:
            break
    
    return bin2str(x[:-16])
    
   