import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "IT\n\nKAVIN", variable = vote, value = "it", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"it",client_socket)).grid(row = 2,column = 1)
    itLogo = ImageTk.PhotoImage((Image.open("img/it.jpeg")).resize((45,45),Image.ANTIALIAS))
    itImg = Label(frame1, image=itLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "ECE\n\nSIVA", variable = vote, value = "ece", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"ece",client_socket)).grid(row = 3,column = 1)
    eceLogo = ImageTk.PhotoImage((Image.open("img/ece.jpg")).resize((35,48),Image.ANTIALIAS))
    eceImg = Label(frame1, image=eceLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "EEE\n\nArvind", variable = vote, value = "eee", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"eee",client_socket) ).grid(row = 4,column = 1)
    eeeLogo = ImageTk.PhotoImage((Image.open("img/eee.png")).resize((55,40),Image.ANTIALIAS))
    eeeImg = Label(frame1, image=eeeLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "MECH\n\nRAGUL", variable = vote, value = "mech", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"mech",client_socket)).grid(row = 5,column = 1)
    mechLogo = ImageTk.PhotoImage((Image.open("img/mech.jpg")).resize((50,45),Image.ANTIALIAS))
    mechImg = Label(frame1, image=mechLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nNOTA    \n  ", variable = vote, value = "nota", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"nota",client_socket)).grid(row = 6,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((45,35),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
