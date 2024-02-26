from tkinter import *
from random import choice

App = Tk()
App.title('Element Picker')
App.geometry('350x100')

inp = Entry(App)
inp.pack()


def pick():
    INP = (inp.get()).split(',')
    msg = Label(App, text=choice(INP))
    msg.pack()


B = Button(App, text='choose', command=pick)
B.pack()

App.mainloop()
