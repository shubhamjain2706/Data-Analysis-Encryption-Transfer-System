import socket
import sys
import time
from Tkinter import *
from PIL import ImageTk,Image

global root
global root2



def IpStore(a=1):
     global root
     root.destroy()
    
def IpStore2(a=1):
     global root
     root2.destroy()
     




def func():
     global root
     global root2   
     root2 = Tk()
     root2.geometry('400x150')
     root2.title('D.A.R.T.S')
     Label(root2,font=('Helvetica',14), text = 'Welcome to').place(x=170,y=20)
     Label(root2,font=('Helvetica',30), text = 'D.A.R.T.S').place(x=150,y=40)
     Button(root2,text = 'Continue', command = IpStore2).place(x=170,y=80) 
     root2.mainloop()
    
    
     root = Tk()
     root.configure(background = 'white') 
     root.title('D.A.R.T.S : Client Setup')  
     root.geometry('500x150') 


     name = StringVar()
     Label(root,font=('Helvetica',14), text = 'Username : ').place(x=100,y=43)
    
     b=Entry(root,textvariable=name, bg = "#c0c0c0",fg='white') 
     b.place(x=210,y=40)
     b.insert(0,'Ex : Sam')
     b.bind("<Return>",IpStore)

     Button(root,text = 'Login', command = IpStore).place(x=210,y=80)   
     root.mainloop()
     return name.get()

