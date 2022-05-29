from tkinter import *
from tkinter.scrolledtext import ScrolledText


def translateFirst(content, c):
    to_add = ">[-]<[-]"
    c += 4.3
    for i in range(ord(content) // 8):
        to_add += "+"
        c += 1
    to_add += "[>++++++++<-]>"
    c += 11.99
    for j in range(ord(content) % 8):
        to_add += "+"
        c += 1
    to_add += ".<"
    c += 1.15

    return to_add, c


def translateRest(value, c):
    to_add = ""
    for i in range(abs(value) // 8):
        to_add += "+"
        c += 1
    if value > 0:
        to_add += "[>++++++++<-]>"
        c += 11.99
    else:
        to_add += "[>--------<-]>"
        c += 7.67

    for j in range(abs(value) % 8):
        if value > 0:
            to_add += "+"
            c += 1
        else:
            to_add += "-"
            c += 0.46

    to_add += ".<"
    c += 1.15

    return to_add, c


def createTranslator(window):
    translator = Toplevel(window)
    translator.title('BrainIDE - Translator')
    translator.config(bg='#5e5e5e')

    to_trans = ScrolledText(translator, background='#2b2b2b', foreground='#808077', font=('JetBrains Mono', 13),
                            undo=True, autoseparators=True, maxundo=-1, width=30, height=10)
    output = ScrolledText(translator, background='#2b2b2b', foreground='#808077', font=('JetBrains Mono', 13),
                          width=30, height=10)

    transMenu = Menu(translator)
    translator.config(menu=transMenu)
    translator.config(bg='black')

    translator.bind('<Shift-F12>', lambda x: translate(to_trans.get('1.0', END), output))

    transMenu.add_command(label='Translate!', command=lambda: translate(to_trans.get('1.0', END), output),
                          accelerator='Shift+F12')

    to_trans.pack(side=TOP, fill=BOTH)
    output.pack(side=TOP, fill=BOTH)


def translate(data, output):
    output.delete('1.0', END)

    aux = 1
    code = ""
    count = 0
    for index, content in enumerate(data):
        if index == 0:
            to_add, count = translateFirst(content, count)
            code += to_add
        else:
            value = ord(content) - ord(data[index - 1])
            to_add, count = translateRest(value, count)
            code += to_add
        if count >= (25 * aux):
            first_part = code[:(35 * aux)]
            second_part = code[(35 * aux):]
            code = first_part + "\n" + second_part
            aux += 1

    output.insert('1.0', code)
