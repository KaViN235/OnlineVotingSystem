import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    itLogo = ImageTk.PhotoImage((Image.open("img/it.jpeg")).resize((35,35),Image.ANTIALIAS))
    itImg = Label(frame1, image=itLogo).grid(row = 2,column = 0)

    eceLogo = ImageTk.PhotoImage((Image.open("img/ece.jpg")).resize((25,38),Image.ANTIALIAS))
    eceImg = Label(frame1, image=eceLogo).grid(row = 3,column = 0)

    eeeLogo = ImageTk.PhotoImage((Image.open("img/eee.png")).resize((45,30),Image.ANTIALIAS))
    eeeImg = Label(frame1, image=eeeLogo).grid(row = 4,column = 0)

    ssLogo = ImageTk.PhotoImage((Image.open("img/mech.jpg")).resize((40,35),Image.ANTIALIAS))
    ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((35,25),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)


    Label(frame1, text="it              :       ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['it'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" ece             :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['ece'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text=" eee               :          ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['eee'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text=" mech    :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['mech'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text=" NOTA            :          ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
        root = Tk()
        root.geometry('500x500')
        frame1 = Frame(root)
        showVotes(root,frame1)
