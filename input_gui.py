import config
from os import chdir
from listcreate import InputListIntoScoutedArray
from filecreate import GetNameAndTeamNum
from filecreate import WriteArrayToText
from Tkinter import mainloop
from Tkinter import IntVar
from Tkinter import Checkbutton
from Tkinter import Button
from Tkinter import Tk
from Tkinter import Entry
from Tkinter import END
master = Tk()
chdir(config.dirScouted)

def callback():
    q = bool(re.get())
    s = bool(re2.get())
    z = bool(re3.get())
    # TODO : use listcreation methods to sanitize the inputs before being placed into a new array
    InfoArray = [e.get(),g.get(),int(h.get()),int(r.get()),q,s,m.get(),z]
    WriteArrayToText(InfoArray)

e = Entry(master)
e.pack()
e.delete(0, END)
e.insert(0, "Team Number")
g = Entry(master)
g.pack()
g.delete(0, END)
g.insert(0, "Team Name")
m = Entry(master)
m.pack()
m.delete(0, END)
m.insert(0, "Match num")
h = Entry(master)
h.pack()
h.delete(0, END)
h.insert(0, "Totes Stacked")
r = Entry(master)
r.pack()
r.delete(0, END)
r.insert(0, "Bins On Totes")
re = IntVar()
re2 = IntVar()
re3 = IntVar()
l = Checkbutton(master, text="Litter", variable=re)
l.pack()
c = Checkbutton(master, text="Chute", variable=re2)
c.pack()
cc = Checkbutton(master, text="Broken", variable=re3)
cc.pack()
b = Button(master, text="Submit", command=callback)
b.pack()
mainloop()
