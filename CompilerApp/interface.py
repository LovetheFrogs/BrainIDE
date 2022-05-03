from tkinter import *
from brainfuck_compiler import *

def clearAll():
    output.delete('1.0', END)
    input.delete('1.0', END)
    editor.delete('1.0', END)


def menuBarCreator():
    menuBar = Menu(window)
    window.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    runMenu = Menu(menuBar, tearoff=0)

    menuBar.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label='New File...', command=newFile)
    fileMenu.add_command(label='Open File...')
    fileMenu.add_separator()
    fileMenu.add_command(label='Save As...')
    fileMenu.add_command(label='Save...')
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=exit)

    menuBar.add_cascade(label='Run', menu=runMenu)
    runMenu.add_command(label='Run...', command=run)
    runMenu.add_command(label='Clear Console', command=lambda: output.delete('1.0', END))


def run():
    output.delete('1.0', END)
    lang, pointer = inicialize()
    code = editor.get('1.0', 'end-1c')
    input_data = input.get('1.0', 'end-1c')

    result = codeReader(lang, code, pointer, input_data)

    output.insert(END, result + '\n')


def newFile():
    clearAll()
    editor.insert('1.0', "NOTE: ALL CHANGES MUST BE SAVED OR ELSE THEY WILL BE DELETED UPON EXITING!!")


def inicializeWindow():
    global window
    window = Tk()

    window.title('BrainIDE')
    window.iconbitmap('.//resources//lovethefrogs.ico')

    window.config(background='#5e5e5e')

    global editor
    editor = Text(background='#0d1117', foreground='white')
    editor.pack(expand=True, fill=BOTH, padx=2.5, pady=(2.5, 1.75))

    global input
    input = Text(background='#0d1117', foreground='white')
    input.pack(expand=True, fill=BOTH, side=LEFT, padx=(2.5, 1.75), pady=(1.75, 2.5))

    global output
    output = Text(background='#0d1117', foreground='white')
    output.bind("<Key>", lambda e: "break")
    output.pack(expand=True, fill=BOTH, side=RIGHT, padx=(1.75, 2.5), pady=(1.75, 2.5))

    # logo = PhotoImage(file='.//resources//lovethefrogs.png')
    # Label(image=logo, background='#5e5e5e', width=300, anchor='center').grid(column=1, row=3)

    menuBarCreator()

    window.mainloop()