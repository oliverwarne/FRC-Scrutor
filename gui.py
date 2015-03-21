from tkinter import mainloop
from tkinter import IntVar
from tkinter import Checkbutton
from tkinter import Button
from tkinter import Tk
from tkinter import Entry
from tkinter import END
master = Tk()

def callback():
    q = bool(re.get())
    s = bool(re2.get())
    InfoArray = [e.get(),g.get(),m.get(),h.get(),r.get(),q,s]
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
h.insert(0, "Totes")
r = Entry(master)
r.pack()
r.delete(0, END)
r.insert(0, "Bins")
re = IntVar()
re2 = IntVar()
l = Checkbutton(master, text="Litter", variable=re)
l.pack()
c = Checkbutton(master, text="Chute", variable=re2)
c.pack()
b = Button(master, text="Submit", command=callback)
b.pack()
mainloop()
