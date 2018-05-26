#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import time
from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
from socket import *
from thread import *
import sys,os
import AES_Encryption
import Self_Made_Encrypt
import DES_Encryption
import RSA_Encryption
import stegnography_encode
import popup_Username
import py_compile
from subprocess import call

host = 'localhost' 
port = 8443
activity=""
global username
global root



def newclient():
    os.chdir("/Library/Frameworks/python.framework/versions/2.7/lib/python2.7/")
    call("python Client_GUI_Final.py",shell=True)

    
def connect():
    self.ConnectButton()
    

def aboutus():
    global root
    root = Tk() 
    root.configure(background = 'white') 
    root.title('D.A.R.T.S : About Us') 
    root.geometry('500x200')  
    Label(root,font=('Helvetica',14), text = 'Project Created by : ').place(x=150,y=20)
    Label(root,font=('Helvetica',14), text = 'Chinmay Phutela - 13103467').place(x=150,y=60)
    Label(root,font=('Helvetica',14), text = 'Sarthak Chauhan - 13103479').place(x=150,y=80)
    Label(root,font=('Helvetica',14), text = 'Shubham Kumar Jain - 13103481').place(x=150,y=100)
    Label(root,font=('Helvetica',14), text = 'Priyanka Johri - 13103499').place(x=150,y=120)
    
    Button(root,text = 'Close', command = root.destroy).place(x=210,y=160)   
    root.mainloop()
    
    
def gethelp():
    global root
    root = Tk()
    root.configure(background = 'white')
    root.title('D.A.R.T.S : Help')  
    root.geometry('500x200')  
    Label(root,font=('Helvetica',14), text = 'Follow the procedure : ').place(x=150,y=20)
    Label(root,font=('Helvetica',14), text = '1. Establish your connection with the server').place(x=150,y=60)
    Label(root,font=('Helvetica',14), text = '2. Select a mode of Encyption for your files').place(x=150,y=80)
    Label(root,font=('Helvetica',14), text = '3. Click Send').place(x=150,y=100)
    Label(root,font=('Helvetica',14), text = '4. Hurray! You have succesfully sent your files').place(x=150,y=120)
   
    Button(root,text = 'Close', command = root.destroy).place(x=210,y=160)  
    root.mainloop()
    

def serverthread():
    global sock,activity,app
    data=sock.recv(100)
    activity=activity+"Message from D.A.R.T.S server : "+data+"\n"
    app.act.set(activity)
    start_new_thread(serverthread,())
    
    

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        """col,row=self.grid_size()
        print row,col"""

        
        frame1=Tkinter.Frame()
        frame1.grid(row=0,column=0, sticky='W',pady=5,padx=5)
        frame2=Tkinter.Frame()
        frame2.grid(row=1,column=0, sticky='W',pady=5,padx=5)
        frame3=Tkinter.Frame()
        frame3.grid(row=2,column=0, sticky='W',pady=5, padx=5)

        #frame 1 settings
        
        self.IPaddr = Tkinter.StringVar()
        IP_label = Tkinter.Label(frame1,textvariable=self.IPaddr,fg="dark gray",bg="#ccff99",font=('Arial', 10,'bold'),width="93")
        IP_label.grid(column="3",row="0",columnspan=3,padx="10",pady="5") 
        self.IPaddr.set("\tStatus : Not Connected\t\t")
        
        #button 'connect'
        button = Tkinter.Button(frame1,text="Connect",bg="dark gray",command=self.ConnectButton,font=('Arial', 10,"bold"),width="10")
        button.grid(column="6",row="0")
        
        
        #frame 2 settings
        
        #Activity Log
        self.act = Tkinter.StringVar()
        act_log = Tkinter.Label(frame2,textvariable=self.act,anchor="nw",bg="light yellow",fg="black",justify="center",relief="ridge",borderwidth=3,font=('Arial', 10,'bold'),width="70",height="15")
        act_log.grid(column="0",row="0",columnspan=2,sticky='W',rowspan="6") 
        self.act.set("\n\t\t\t\tD.A.R.T.S Activity Log\t\t\t")
        
        #File location label
        self.file = Tkinter.StringVar()
        file_loc = Tkinter.Entry(frame2,textvariable=self.file,fg="black",bg="#9999cc",relief="ridge",borderwidth=1,width="40",font=('Arial', 10))
        file_loc.grid(column="2",row="0",columnspan=2,padx="10",sticky='W') 
        self.file.set("\tEnter the File Path Here\t\t\t")
        
        #button 'Browse'
        browse_button = Tkinter.Button(frame2,text="Browse",width="10",bg="light green",command=self.BrowseButton,font=('Arial', 10,"bold"))
        browse_button.grid(column="3",row="1",columnspan=2,sticky='W')

        #button 'AES'
        self.var=IntVar()
        AES_button = Tkinter.Radiobutton(frame2,text="AES",variable=self.var,value=1,command=self.Enc_Button)
        AES_button.grid(column="2",row="3",padx="10",sticky='W')
        self.var.set(1)
        
        #button 'Self_made'
        Self_made_button = Tkinter.Radiobutton(frame2,text="Self Made",variable=self.var,value=2,command=self.Enc_Button)
        Self_made_button.grid(column="2",row="4",padx="10",sticky='W')
        self.var.set(2)
        
        
        #button 'DES'
        DES_button = Tkinter.Radiobutton(frame2,text="DES",variable=self.var,value=3,command=self.Enc_Button)
        DES_button.grid(column="3",row="3",padx="10",sticky='W')
        self.var.set(3)

        #button 'RSA'
        RSA_button = Tkinter.Radiobutton(frame2,text="RSA",variable=self.var,value=4,command=self.Enc_Button)
        RSA_button.grid(column="3",row="4",padx="10",sticky='W')
        self.var.set(4)

        
        
        #button 'Send File'
        file_send_button = Tkinter.Button(frame2,state="normal",text="Send File",bg="red",command=self.FileSendButton,width="37",font=('Arial', 10,"bold"))
        file_send_button.grid(column="2",row="5",columnspan=2,padx="10",sticky='W')
        
        #frame 3 settings
        #button 'Send Text'
        text_send_button = Tkinter.Button(frame3,state="normal",text="Send Text",command=self.TextSendButton,font=('Arial', 10,"bold"),width="15",height="1")
        text_send_button.grid(column=2,row=0,padx=6)
        
        #Text display
        self.text_bar = Tkinter.StringVar()
        self.text_label = Tkinter.Entry(frame3,textvariable=self.text_bar,fg="black",bg="light gray",width="49",font=('Arial', 10))
        self.text_label.grid(column="0",columnspan=2,row="0",pady="10") 
        self.text_label.bind("<Return>", self.OnPressEnter)
        self.text_bar.set("\t\tSend us your feedback")

        
        #screen
        self.geometry("700x290")
        self.resizable(False,False)
        self.update()
        self.geometry(self.geometry())
        self.text_label.focus_set()
        self.text_label.selection_range(0, Tkinter.END)
        

        #Server Connection
    def ConnectButton(self):
        global activity
        global sock
        global username
        sock = socket()
        sock.connect((host, port))
        sock.send(username)
        start_new_thread(serverthread,())
       
        self.IPaddr.set(" Status : Connected to "+host)
        activity="Status : Connected to "+host+"\n"
        self.act.set(activity)
        
        
    def BrowseButton(self):
        global activity
        Tk().withdraw() 
        global filename
        filename = askopenfilename()
        print(filename)
        self.file.set(filename)
        directory ,file_name=os.path.split(filename)
        if filename:
            activity=activity+"File Selected : "+file_name+"\n"
            self.act.set(activity)

    def FileSendButton(self):
        global activity
        global filename,sock
        global username
        
        if self.var.get()==1:
            enc_file_name=AES_Encryption.AESEncryption(filename)
        elif self.var.get()==2:
            enc_file_name=Self_Made_Encrypt.Image_Encrypt(filename)
        elif self.var.get()==3:
            enc_file_name=DES_Encryption.DESEncryption(filename)    
        elif self.var.get()==4:
            print "yo"
            enc_file_name=RSA_Encryption.RSAEncryption(filename)
            
        enc_file_addr="encrypted files/"+enc_file_name
        activity=activity+"Sending.... \n"
        self.act.set(activity)
        sock.send(str(self.var.get())+enc_file_name)
        
        f=open(enc_file_addr, "rb") 
        l = f.read(1024)
        while (l):
            sock.send(l)
            l = f.read(1024)
        sock.close()
      
        sock = socket()
        sock.connect((host, port))
        sock.send(username)
        activity=activity+"Transfer Complete \n"
        self.act.set(activity)
        self.file.set("\tEnter the File Path Here")
        
        
        
    def TextSendButton(self):
        global activity
        global username
        global sock
        message=self.text_bar.get()
       
        activity=activity+"Message Delivered : "+message+"\n"
        self.act.set(activity)
        steg_file_name=stegnography_encode.encode(message)
        steg_file_addr='stegnographed_files/'+steg_file_name
       
        sock.send(str(5)+steg_file_name)
        
        f=open(steg_file_addr, "rb") 
        l = f.read(1024)
        while (l):
            sock.send(l)
            l = f.read(1024)
        sock.close()
        
        sock=socket()
        sock.connect((host,port))
        sock.send(username)
        
        self.act.set(activity)
        self.text_bar.set("")
        
        

    def OnPressEnter(self,event):
        global activity
        global sock
       
        
    def Enc_Button(self):
        #print self.var.get()
        
    
        
if __name__ == "__main__":
   
    client="Client"
    global username,app
  
    username=popup_Username.func()
    app = simpleapp_tk(None)
    app.title("D.A.R.T.S : Client " + username)
    
    menu = Menu(app)
    app.config(menu=menu)

    subMenu = Menu(menu)
   
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Client", command=newclient)
    subMenu.add_command(label="Connect to Server", command=connect)
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=app.quit)

    editMenu = Menu(menu)
    menu.add_cascade(label="View", menu=editMenu)
    editMenu.add_command(label="About Us", command=aboutus)
    editMenu.add_separator()
    editMenu.add_command(label="Help", command=gethelp)

    app.mainloop()


    
    
    
    
