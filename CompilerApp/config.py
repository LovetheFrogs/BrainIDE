from tkinter import *
from tkinter.colorchooser import askcolor


def createConfig(window, colormap, opt):
    global config
    global container

    config = Toplevel(window)
    config.title('BrainIDE - Config')
    config.config(bg='#3b3b3b')

    if opt == 1:
        colorFormat(colormap)


def colorFormat(colormap):
    global pic

    pic = PhotoImage(file='resources//separator.png')
    lab = Label(config, image=pic, bg='#3b3b3b', height=2, width=500)
    lab.grid(row=1, columnspan=6)

    Label(config, text='Change the color of the different brainfuck symbols.',
          background='#3b3b3b', foreground='#808077', font=('JetBrains Mono', 13)).grid(column=0, columnspan=6, row=0)

    Label(config, text='[', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=0, row=2, pady=(3, 0))
    Label(config, text='[', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=4, row=2, pady=(3, 0))

    Label(config, text='+', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=0, row=3)
    Label(config, text='-', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=4, row=3)

    Label(config, text='>', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=0, row=4)
    Label(config, text='<', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=4, row=4)

    Label(config, text='.', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=0, row=5)
    Label(config, text=',', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=4, row=5)

    Button(config, bg=colormap['['], command=lambda: alterColor('[', colormap)).grid(column=1, row=2, pady=3)
    Button(config, bg=colormap[']'], command=lambda: alterColor(']', colormap)).grid(column=5, row=2, pady=3)

    Button(config, bg=colormap['+'], command=lambda: alterColor('+', colormap)).grid(column=1, row=3, pady=3)
    Button(config, bg=colormap['-'], command=lambda: alterColor('-', colormap)).grid(column=5, row=3, pady=3)

    Button(config, bg=colormap['>'], command=lambda: alterColor('>', colormap)).grid(column=1, row=4, pady=3)
    Button(config, bg=colormap['<'], command=lambda: alterColor('<', colormap)).grid(column=5, row=4, pady=3)

    Button(config, bg=colormap['.'], command=lambda: alterColor('.', colormap)).grid(column=1, row=5, pady=3)
    Button(config, bg=colormap[','], command=lambda: alterColor(',', colormap)).grid(column=5, row=5, pady=3)


def alterColor(altered, colormap):
    new = askcolor(color=None)
    colormap[altered] = new[1]
