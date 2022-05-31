# Have to ask whether to use two different windows or just one for table + conversor below it.
from tkinter import *


def openTable(window):
    global pic
    global char
    global value

    ASCIIWindow = Toplevel(window)
    ASCIIWindow.config(bg='#2b2b2b')
    ASCIIWindow.title('ASCII Table + Converter')

    pic = PhotoImage(file='resources//ASCIITable.png')
    lab = Label(ASCIIWindow, image=pic)
    lab.grid(row=0, columnspan=5)

    Label(ASCIIWindow, text='Char', bg='#2b2b2b', foreground='#808077',
          font=('JetBrains Mono', 10)).grid(column=0, row=1)
    char = Entry(ASCIIWindow, width=30, bg='#3b3b3b', foreground='#808077', font=('JetBrains Mono', 10))
    char.focus_set()
    char.grid(column=1, row=1)

    Label(ASCIIWindow, text='Value', bg='#2b2b2b', foreground='#808077',
          font=('JetBrains Mono', 10)).grid(column=2, row=1)
    value = Entry(ASCIIWindow, width=30, bg='#3b3b3b', foreground='#808077', font=('JetBrains Mono', 10))
    value.bind("<Key>", lambda e: "break")
    value.grid(column=3, row=1)

    char.bind('<KeyPress>', enterPressed)
    Button(ASCIIWindow, text='Convert!', bg='#3b3b3b', foreground='#808077', activebackground='#2b2b2b',
           activeforeground='#808077', font=('JetBrains Mono', 10),
           command=convert).grid(column=4, row=1)


def convert():
    value.delete(0, END)
    value.config(foreground='#808077')
    to_ASCII = char.get()
    if len(to_ASCII) == 1:
        value.insert(END, ord(to_ASCII))
    else:
        value.config(foreground='red')
        value.insert(END, 'ERROR')


def enterPressed(event):
    if event.char == '\r':
        convert()
    elif event.char != '':
        char.delete(0, END)
