from PIL import Image
import os
img1=""
pixels=[]

def red(i,j):
    global pixels
    
    return pixels[i,j][0]

def green(i,j):
    global pixels
    return pixels[i,j][1]

def blue(i,j):
    global pixels
    return pixels[i,j][2]


def blocks_xor():
    global img1,pixels
    x=img1.size[0]
    y=img1.size[1]
    x1=0
    y1=0
    x2=x/2
    y2=y/2
    
    for i in range (x-1,x2-1,-1):
        for j in range (y-2,y2-1,-1):
            a= red(i,j)^red(i,j+1)
            b= green(i,j)^green(i,j+1)
            c= blue(i,j)^blue(i,j+1)
            pixels[i,j]=(a,b,c)

    
    for i in range(x2):
        for j in range(y2,y):
            a= red(i,j)^red(x2+i,j)
            b= green(i,j)^green(x2+i,j)
            c= blue(i,j)^blue(x2+i,j)
            pixels[i,j]=(a,b,c)

    for i in range(x2,x):
        for j in range(y2):
            a= red(i,j)^red(i,y2+j)
            b= green(i,j)^green(i,y2+j)
            c= blue(i,j)^blue(i,y2+j)
            pixels[i,j]=(a,b,c)

    for i in range(x2):
        for j in range(y2):
            a= red(i,j)^red(i,y2+j)
            b= green(i,j)^green(i,y2+j)
            c= blue(i,j)^blue(i,y2+j)
            pixels[i,j]=(a,b,c)

def Image_Decrypt(filename):
    global img1,pixels
    img1=Image.open(filename)
    array=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    
    pixels = img1.load() 
    blocks_xor()
    for i in range(img1.size[0]):    
        for j in range(img1.size[1]):
            temp=str('{0:08b}'.format(pixels[i,j][0]))
            temp1=int(temp[0:4],2)
            temp2=int(temp[4:8],2)
            a=temp2*16+temp1
            temp=str('{0:08b}'.format(pixels[i,j][1]))
            temp1=int(temp[0:4],2)
            temp2=int(temp[4:8],2)
            b=temp2*16+temp1
            temp=str('{0:08b}'.format(pixels[i,j][2]))
            temp1=int(temp[0:4],2)
            temp2=int(temp[4:8],2)
            c=temp2*16+temp1
           
            pixels[i,j]=(a,b,c)
            
            
    directory,file_name=os.path.split(filename)
    print filename,file_name
    img1.save(filename)
