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
    print x,y,x1,y1,x2,y2


    for i in range(x2):
        for j in range(y2):
            a= red(i,j)^red(i,y2+j)
            b= green(i,j)^green(i,y2+j)
            c= blue(i,j)^blue(i,y2+j)
            pixels[i,j]=(a,b,c)
    
    for i in range(x2,x):
        for j in range(y2):
            a= red(i,j)^red(i,y2+j)
            b= green(i,j)^green(i,y2+j)
            c= blue(i,j)^blue(i,y2+j)
            pixels[i,j]=(a,b,c)

    for i in range(x2):
        for j in range(y2,y):
            a= red(i,j)^red(x2+i,j)
            b= green(i,j)^green(x2+i,j)
            c= blue(i,j)^blue(x2+i,j)
            pixels[i,j]=(a,b,c)

    for i in range (x2,x):
        for j in range (y2,y-1):
            a= red(i,j)^red(i,j+1)
            b= green(i,j)^green(i,j+1)
            c= blue(i,j)^blue(i,j+1)
            pixels[i,j]=(a,b,c)
       
            
def Image_Encrypt(filename):
    global img1,pixels
    img1=Image.open(filename)
    array=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    l=0
    
    pixels = img1.load()
    for i in range(img1.size[0]):   
        for j in range(img1.size[1]):
            temp=pixels[i,j][0]%16
            temp1=pixels[i,j][0]/16
           
            a=int(array[temp]+array[temp1],2)
            temp=pixels[i,j][1]%16
            temp1=pixels[i,j][1]/16
            b=int(array[temp]+array[temp1],2)
            temp=pixels[i,j][2]%16
            temp1=pixels[i,j][2]/16
            c=int(array[temp]+array[temp1],2)
            
            pixels[i,j]=(a,b,c)
            
            
            
    blocks_xor()
    directory1="encrypted files"
    if not os.path.exists(directory1):
        os.makedirs(directory1)
    directory1=directory1+'/'
    directory,file_name=os.path.split(filename)
    file_name,ext=os.path.splitext(file_name)
    img1.save(directory1+file_name+'.png')
    return file_name+'.png'
