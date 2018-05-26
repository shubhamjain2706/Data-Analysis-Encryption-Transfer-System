#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
from socket import *
from thread import *
import sys,os
import AES_Decryption
import Self_Made_Decrypt
import stegnography_decode
import DES_Decryption
import RSA_Decryption



host = 'localhost'  
port = 8443

object
sock = socket()

sock.bind((host, port))

sock.listen(10) 

global client
global clientaddr
global clientname
clientaddr=[]
client=[]
clientname=[]

activity=""


def start(a=1):
    global client,activity
    global app
    global clientaddr
    global clientname
    while True:
    
        conn, addr = sock.accept()
        name=conn.recv(10)
        clientname.append(name)
        client.append(conn)
        clientaddr.append(addr)
        activity=activity+"Connected to "+name+" with address "+str(addr)+" \n"
        app.act.set(activity)
        print conn, addr
        
        app.update_optionlist()
        
        start_new_thread(clientthread,(conn,)) 

def clientthread(conn):
    global client,clientaddr,clientname,app,activity
    
    message=conn.recv(50)
    message_type=int(message[0])
    file_name=message[1:]
    print "MESSAGE TYPE -> "+str(message_type)
    
    print message_type
    if (message_type==1 or message_type==2 or message_type==3 or message_type==4):
        
        directory="received_files"
        if not os.path.exists(directory):
            os.makedirs(directory)
        directory=directory+"/"
        print file_name
        print "Start Receiving File"
        
        activity=activity+"Receiving file from : Client "+clientname[client.index(conn)]+"\n"
        app.act.set(activity)
        f = open(directory+str(file_name),'wb')
        l = conn.recv(1024)
        while (l):
            f.write(l)
            l = conn.recv(1024)
        f.close()
        print "file received"
        
        activity=activity+"Received file from :"+clientname[client.index(conn)]+"\n"+"Decrypting File: "+file_name+"\n"
        app.act.set(activity)
        
        if message_type==1:
            print "Decrypting AES file " +file_name
            AES_Decryption.AESDecryption(directory+str(file_name))
            print " File AES Decrypted"
        elif message_type==2:
            print "Decrypting Self_made file"+ file_name
            Self_Made_Decrypt.Image_Decrypt(directory+str(file_name))
            print " File Self_Made Decrypted"
        elif message_type==3:
            print "Decrypting DES file"+ file_name
            DES_Decryption.DESDecryption(str(file_name))
            print " File DES Decrypted"
        elif message_type==4:
            print "Decrypting RSA file"+ file_name
            RSA_Decryption.RSADecryption(str(file_name)) 
            print " File RSA Decrypted"
        activity=activity+"File Decrypted : "+file_name+"\n"
        app.act.set(activity)
        
    elif (message_type==5):
        
        directory="received_stegnography_files"
        if not os.path.exists(directory):
            os.makedirs(directory)
        directory=directory+"/"
        print "Start Receiving stegnographed File"
        activity=activity+"Receiving encrypted message file from :"+clientname[client.index(conn)]+"\n"
        app.act.set(activity)
        
        f = open(directory+str(file_name),'wb')
        l = conn.recv(1024)
        while (l):
            f.write(l)
            l = conn.recv(1024)
        f.close()
        activity=activity+"Received encrypted message : "+clientname[client.index(conn)]+"\n"+"Decrypting Message\n"
        app.act.set(activity)
         message=stegnography_decode.decode(directory+str(file_name))
        print " Text DECODED" 
        activity=activity+"MESSAGE : "+message+"\n"
        app.act.set(activity)
        
        print "Data Received Is :-> "+message
        
    del clientaddr[client.index(conn)]
    del clientname[client.index(conn)]
    client.remove(conn)
    
    app.update_optionlist()
    """else:
        message=conn.recv(1024)
        print "client: ",str(message)"""


class simpleapp_tk(Tkinter.Tk):    
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        
        frame1=Tkinter.Frame()
        frame1.grid(row=0,column=0, sticky='W',pady=5,padx=5)
        frame2=Tkinter.Frame()
        frame2.grid(row=1,column=0, sticky='W',pady=5,padx=5)
        frame3=Tkinter.Frame()
        frame3.grid(row=2,column=0, sticky='W',pady=5, padx=5)

        #frame 1 settings
        #button 'Send Text'
        text_send_button = Tkinter.Button(frame1,state="normal",text="Send Text",command=self.TextSendButton,font=('Arial', 10,"bold"),width="15",height="1")
        text_send_button.grid(column=1,row=4,sticky='W')
        
        #Text display
        self.text_bar = Tkinter.StringVar()
        self.text_label = Tkinter.Entry(frame1,textvariable=self.text_bar,fg="black",bg="light gray",relief="ridge",borderwidth=3,width="50",font=('Arial', 10))
        self.text_label.grid(column="0",row="4",padx="10") 
        self.text_label.bind("<Return>", self.OnPressEnter)
        self.text_bar.set("\t\tEnter your text here")

        #button 'Broadcast'
        self.varText=IntVar()
        BroadcastText = Tkinter.Radiobutton(frame1,text="Broadcast",variable=self.varText,value=1,command=self.Enc_Button)
        BroadcastText.grid(column="0",row="1",padx="1",sticky='W')
        self.varText.set(1)
        
        #button 'Unicast/Multicast'
        Unicast = Tkinter.Radiobutton(frame1,text="Unicast/Multicast",variable=self.varText,value=2,command=self.Enc_Button)
        Unicast.grid(column="0",row="0",padx="1",sticky='W')
        
        
        #Unicast list
        global clientname
        global option_list
        #print "hiiiiiii"
        self.var2 = StringVar()
        self.var2.set('Select Client')
        option_list = Tkinter.OptionMenu(frame1,self.var2,clientname)
     
        option_list.grid(column="1",row="0",sticky='W')

      
        #Label
        self.str_Label1 = Tkinter.StringVar()
        Label1 = Tkinter.Label(frame2,textvariable=self.str_Label1,fg="black",bg="#ccff99",relief="ridge",borderwidth=3,width="72",font=('Arial', 10,'bold'))
        Label1.grid(column="0",row="0",padx=10) 
        self.str_Label1.set("\tActivity Log\t\t\t")
        
        #frame 3 settings
        
        #Activity Log
        self.act = Tkinter.StringVar()
        act_log = Tkinter.Label(frame3,textvariable=self.act,anchor="nw",bg="light yellow",fg="black",justify="left",relief="ridge",borderwidth=3,font=('Arial', 10),width="72",height="33")
        act_log.grid(column="0",row="0",sticky='W',rowspan="15",columnspan="3",padx=10) 
        
        
       
        #screen
        self.geometry("470x500")
        self.resizable(False,False)
        self.update()
        self.geometry(self.geometry())
        self.text_label.focus_set()
        self.text_label.selection_range(0, Tkinter.END)

        self.update_optionlist()

    

        #Server Connection
   
        
        
    def update_optionlist(self):
        global clientname
        global option_list
        self.var2.set('Client List')
        option_list['menu'].delete(0,'end')
        for cl in clientname:
            option_list['menu'].add_command(label=cl,command=Tkinter._setit(self.var2,cl))
        
    def TextSendButton(self):
        global activity
        global sock
        global client,clientaddr,clientname
        message=self.text_bar.get()
       
        activity=activity+"Msg Sent: "+message+"\n"
        self.act.set(activity)
        self.text_bar.set("")
        print "clients in the list are"
        print client
        if(self.varText.get()==1):
            for x in client:
                x.send(message)
        elif(self.varText.get()==2):
            i=clientname.index(self.var2.get())
            client[i].send(message)
        #print self.text_bar.get()
        
        
    def OnPressEnter(self,event):
        global activity
        global sock
        global client,clientaddr,clientname
        if(self.varText.get()==1):
            message='3'+self.text_bar.get()
        elif(self.varText.get()==2):
            message='4'+self.text_bar.get()
        activity=activity+"\nMsg Sent"
        self.act.set(activity)
        self.text_bar.set("")
        print "clients in the list are"
        print client
        if(self.varText.get()==1):
            for x in client:
                x.send(message)
        elif(self.varText.get()==2):
            i=clientname.index(self.var2.get())
            client[i].send(message)
        
    def Enc_Button(self):
        """global enc_type
        enc_type=self.var.get()"""
    
        
if __name__ == "__main__":
    
    server="D.A.R.T.S : Server"
    start_new_thread(start,(None,))
    global app
    app = simpleapp_tk(None)
    app.title(server)
    app.mainloop()
