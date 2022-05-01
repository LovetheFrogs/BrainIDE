from tkinter import *
from brainfuck_compiler import *

window = Tk()
window.geometry('960x750')
window.title('First GUI')
window.iconbitmap('./lovethefrogs.ico')

window.config(background='#5e5e5e')

helper_editor = Label(window, text="Input", background='#5e5e5e', width=200, font=('Arial', 10), anchor='w')
helper_editor.grid(row=0)

editor = Text(background='#3e3e3e', foreground='white', height=42, width=200)
editor.grid(column=0, row=1)

helper_output = Label(window, text="Output", background='#5e5e5e', width=200, font=('Arial', 10), anchor='w')
helper_output.grid(row=2)

output = Text(background='#3e3e3e', foreground='white', height=16, width=200)
output.grid(column=0, row=3)

logo = PhotoImage(file='lovethefrogs.png')
Label(image=logo, background='#5e5e5e', width=300, anchor='center').grid(column=1, row=3)


def menuBarCreator():
    menuBar = Menu(window)
    window.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    runMenu = Menu(menuBar, tearoff=0)

    menuBar.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label='New File...')
    fileMenu.add_command(label='Open File...')
    fileMenu.add_separator()
    fileMenu.add_command(label='Save As...')
    fileMenu.add_command(label='Save...')
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit')

    menuBar.add_cascade(label='Run', menu=runMenu)
    runMenu.add_command(label='Run...', command=run)
    runMenu.add_command(label='Clear Console', command=lambda: output.delete('1.0', END))


def run():
    lang, pointer = inicialize()
    code = editor.get('1.0', 'end-1c')
    input_data = output.get('1.0', 'end-1c')

    result = codeReader(lang, code, pointer, input_data)

    output.insert(END, '\n\n' + "OUTPUT:")
    output.insert(END, '\n' + result)


menuBarCreator()

window.mainloop()
