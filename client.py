# Import all the required  modules
import os
import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

# Port config
HOST = os.getenv('SOCKET_HOST', '127.0.0.1')
PORT = int(os.getenv('SOCKET_PORT', 5000))
ADDRESS = (HOST, PORT)
FORMAT = "utf-8"
 
# Create a server socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
 
 
# GUI class for the chat
class GUI:
    # constructor method
    def __init__(self):
        # chat window which is currently hidden
        self.tk = Tk()
        self.tk.withdraw()
         
        # login window
        self.startPage = Toplevel()
        # set the title
        self.startPage.title("Login")
        self.startPage.resizable(width = False, height = False)
        self.startPage.configure(width = 400, height = 300)
        # create a Label
        self.labelName = Label(self.startPage,
                               text = "Nome: ",
                               font = "Helvetica 12")
         
        self.labelName.place(relheight = 0.2,
                             relx = 0.1,
                             rely = 0.2)
         
        # create a entry box for
        # typing the message
        self.inputName = Entry(self.startPage,
                             font = "Helvetica 14")

        self.inputName.bind('<Return>', self.pressEnterName)
 
        self.inputName.place(relwidth = 0.4,
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.2)
         
        # set the focus of the curser
        self.inputName.focus()
         
        # create a Continue Button
        # along with action
        self.go = Button(self.startPage,
                         text = "Entrar no Chat",
                         font = "Helvetica 14 bold",
                         command = lambda: self.goAhead(self.inputName.get()))
         
        self.go.place(relx = 0.4,
                      rely = 0.55)
     
        self.tk.mainloop()

    def goAhead(self, name):
        self.startPage.destroy()
        self.layout(name)

        # the thread to receive messages
        recv = threading.Thread(target=self.receive)
        recv.start()
        
    # The main layout of the chat
    def layout(self,name):

        self.name = name
        # to show chat window
        self.tk.deiconify()
        self.tk.title("CHAT-ROOM")
        self.tk.resizable(width = True,
                              height = False)
        self.tk.configure(width = 770,
                              height = 550,
                              bg = "#17202A")
        self.showName = Label(self.tk,
                             bg = "#17202A",
                              fg = "#EAECEE",
                              text = self.name ,
                               font = "Helvetica 13 bold",
                               pady = 5)
         
        self.showName.place(relwidth = 1)
        self.line = Label(self.tk,
                          width = 450,
                          bg = "#ABB2B9")
         
        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)
         
        self.textCons = Text(self.tk,
                             width = 20,
                             height = 2,
                             bg = "#17202A",
                             fg = "#EAECEE",
                             font = "Helvetica 14",
                             padx = 5,
                             pady = 5)
         
        self.textCons.place(relheight = 0.745,
                            relwidth = 1,
                            rely = 0.08)
         
        self.labelBottom = Label(self.tk,
                                 bg = "#ABB2B9",
                                 height = 80)
         
        self.labelBottom.place(relwidth = 1,
                               rely = 0.825)
         
        self.inputMsg = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")

        self.inputMsg.bind('<Return>',self.pressEnterText)


        # place the given widget
        # into the gui window
        self.inputMsg.place(relwidth = 0.74,
                            relheight = 0.06,
                            rely = 0.008,
                            relx = 0.011)
         
        self.inputMsg.focus()

        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text = "Enviar",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.inputMsg.get()))
         
        self.buttonMsg.place(relx = 0.77,
                             rely = 0.008,
                             relheight = 0.06,
                             relwidth = 0.22)
         
        self.textCons.config(cursor = "arrow")
         
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
         
        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight = 1,
                        relx = 0.974)
         
        scrollbar.config(command = self.textCons.yview)
        self.textCons.config(state = DISABLED)
 
    # function to start the thread for sending messages
    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        self.msg = msg
        self.inputMsg.delete(0, END)
        sendMessageThr = threading.Thread(target = self.sendMessage)
        sendMessageThr.start()
 
    # function to receive messages
    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)
                 
                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    client.send(self.name.encode(FORMAT))
                else:
                    # insert messages to text box
                    self.textCons.config(state = NORMAL)
                    self.textCons.insert(END,
                                         message+"\n\n")
                     
                    self.textCons.config(state = DISABLED)
                    self.textCons.see(END)
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                client.close()
                break
    
    # function to send messages
    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            break  

    #Key shortcuts
    def pressEnterText(self, event):
      self.sendButton(self.inputMsg.get())
    
    def pressEnterName(self, event):
      self.goAhead(self.inputName.get())

# create a GUI class object
g = GUI()
