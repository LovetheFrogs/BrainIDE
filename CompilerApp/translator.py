from tkinter import *
from tkinter.scrolledtext import ScrolledText


def createTranslator(window):
    translator = Toplevel(window)
    translator.title('BrainIDE - Translator')
    translator.config(bg='#5e5e5e')
    translator.resizable(False, False)

    to_trans = ScrolledText(translator, background='#2b2b2b', foreground='white', font=('JetBrains Mono', 10),
                            undo=True, autoseparators=True, maxundo=-1, width=50, height=10)
    output = ScrolledText(translator, background='#2b2b2b', foreground='white', font=('JetBrains Mono', 10),
                          width=50, height=10)
    output.bind("<Key>", lambda e: "break")

    transMenu = Menu(translator)
    translator.config(menu=transMenu)
    translator.config(bg='black')

    translateOpt= Menu(transMenu, tearoff=0)

    translator.bind('<Shift-F12>', lambda x: translate(to_trans.get('1.0', END), output))

    transMenu.add_cascade(label='Translator...', menu=translateOpt)
    translateOpt.add_command(label='Translate!', command=lambda: translate(to_trans.get('1.0', END), output),
                             accelerator='Shift+F12')
    translateOpt.add_command(label='Copy Output', command=lambda: copyOutput(window, output), accelerator='Ctrl+Shift+C')
    transMenu.add_command

    to_trans.pack(side=TOP, fill=BOTH)
    output.pack(side=TOP, fill=BOTH)


def translate(data, output):
    output.delete('1.0', END)
    code = ""
    for index, content in enumerate(data):
        if index == 0:
            code += translateFirst(content)
        else:
            value = ord(content) - ord(data[index - 1])
            code += translateRest(value)

    output.insert('1.0', code)


def translateFirst(content):
    to_add = ">[-]<[-]"
    for i in range(ord(content) // 8):
        to_add += "+"
    to_add += "[>++++++++<-]>"
    for j in range(ord(content) % 8):
        to_add += "+"
    to_add += ".<"

    return to_add


def translateRest(value):
    to_add = ""
    for i in range(abs(value) // 8):
        to_add += "+"
    if value > 0:
        to_add += "[>++++++++<-]>"
    else:
        to_add += "[>--------<-]>"

    for j in range(abs(value) % 8):
        if value > 0:
            to_add += "+"
        else:
            to_add += "-"

    to_add += ".<"

    return to_add


def copyOutput(window, output):
    window.clipboard_clear()
    window.clipboard_append(output.get('1.0', END))
