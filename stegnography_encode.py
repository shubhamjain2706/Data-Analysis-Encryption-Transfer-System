#import numpy
from PIL import Image
import os
import binascii

def str2bin(message):
    binary=bin(int(binascii.hexlify(message),16))
    print binary
    return binary[2:]


def encode(message):
    img1=Image.open('image_stegnography.jpg')
    binary=str2bin(message)+"1111111111111110"
    pixels = img1.load()
    x=0
    for i in range(img1.size[0]):    # for every pixels:
        for j in range(img1.size[1]):
            r,g,b=bin(pixels[i,j][0]),bin(pixels[i,j][1]),bin(pixels[i,j][2])
            #print pixels[i,j],r,g,b
            #print bin(pixels[i,j][0])[-1]
            if x<len(binary):
                r=bin(pixels[i,j][0])[:-1]+binary[x]
                x=x+1
                r=int(r,2)
                g,b=int(g,2),int(b,2)
                pixels[i,j]=(r,g,b)
            else:
                #print "red"
                break
            #for green    
            if x<len(binary):
                g=bin(pixels[i,j][1])[:-1]+binary[x]
                x=x+1
                g=int(g,2)
                pixels[i,j]=(r,g,b)
            else:
                #print "green"
                #g,b=int(g,2),int(b,2)
                pixels[i,j]=(r,g,b)
                break
            # for blue
            if x<len(binary):
                b=bin(pixels[i,j][2])[:-1]+binary[x]
                x=x+1
                b=int(b,2)
                pixels[i,j]=(r,g,b)
            else:
                #print "blue"
                #b=int(b,2)
                pixels[i,j]=(r,g,b)
                break
            #print pixels[i,j],binary[x-3],binary[x-2],binary[x-1],x
        
        if x>=len(binary):
            #print pixels[i,j],binary[x-3],binary[x-2],binary[x-1],x
            break
    directory1="stegnographed_files"
    if not os.path.exists(directory1):
        os.makedirs(directory1)
    directory1=directory1+'/'
    img1.save(directory1+'stegnographed.tif')
    return 'stegnographed.tif'

#img1.show()
