from kahoot import *
from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.geometry("200x250")
root.resizable(False, False)
root.title("Kahoot Raider")

RAID_CLIENTS = [
    5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100
]
default = StringVar(root)
default.set(RAID_CLIENTS[0])

pinL = Label(root, text="Game PIN:")
pinE = Entry(root)
nameL = Label(root, text="Username:")
nameE = Entry(root)
info = Label(root, text="(Use #id# to print clients ID number)", font=tkFont.Font(size=7))
clientsL = Label(root, text="Client Count:")
clientsE = OptionMenu(root, default, *RAID_CLIENTS)

pinL.pack()
pinE.pack()
spacing = Label(root, text="")
spacing.pack()
nameL.pack()
nameE.pack()
info.pack()
spacing = Label(root, text="")
spacing.pack()
clientsL.pack()
clientsE.pack()
spacing = Label(root, text="")
spacing.pack()

def SpamKahoot():
    i = 1

    rawUN = nameE.get()
    while i <= int(default.get()):
        if rawUN.count('#id#') >= 1:
            username = rawUN.replace('#id#', str(i))
            bot = client()
            bot.join(pinE.get(),username)
        else:
            username = rawUN + str(i)
            bot = client()
            bot.join(pinE.get(),username)
        i += 1

raidB = Button(root, text="Raid Kahoot!", command=SpamKahoot)
raidB.pack()

root.mainloop()
