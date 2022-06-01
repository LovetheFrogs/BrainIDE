from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import pickle


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

    Label(config, text='Change the color of the different brainfuck symbols.',
          background='#3b3b3b', foreground='#808077', font=('JetBrains Mono', 13)).grid(column=0, columnspan=6, row=0)
    Label(config, text='(restarting required after changing colors)',
          background='#3b3b3b', foreground='#808077', font=('JetBrains Mono', 7)).grid(column=0, columnspan=4, row=5)

    pic = PhotoImage(file='resources//separator.png')
    lab = Label(config, image=pic, bg='#3b3b3b', height=2, width=500)
    lab.grid(row=1, columnspan=6)

    Label(config, text='[', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=0, row=2, pady=(3, 0))
    Label(config, text='[', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=4, row=2, pady=(3, 0))

    Label(config, text='+ and -', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=0, row=3)

    Label(config, text='> and <', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=4, row=3)

    Label(config, text='. and ,', background='#3b3b3b', foreground='#808077',
          font=('JetBrains Mono', 13)).grid(column=2, row=4)

    lb_button = Button(config, bg=colormap['['], activebackground=colormap['['],
                       command=lambda: alterColor(['['], colormap, lb_button))
    lb_button.grid(column=1, row=2, pady=3)
    rb_button = Button(config, bg=colormap[']'], activebackground=colormap[']'],
                       command=lambda: alterColor([']'], colormap, rb_button))
    rb_button.grid(column=5, row=2, pady=3)

    p_button = Button(config, bg=colormap['+'], activebackground=colormap['+'],
                      command=lambda: alterColor(['+', '-'], colormap, p_button))
    p_button.grid(column=1, row=3, pady=3)

    lt_button = Button(config, bg=colormap['>'], activebackground=colormap['>'],
                       command=lambda: alterColor(['>', '<'], colormap, lt_button))
    lt_button.grid(column=5, row=3, pady=3)

    pnt_button = Button(config, bg=colormap['.'], activebackground=colormap['.'],
                        command=lambda: alterColor(['.', ','], colormap, pnt_button))
    pnt_button.grid(column=3, row=4, pady=3)

    Button(config, text='Restore default',  bg='#3b3b3b', activebackground='#4b4b4b', foreground='#808077',
           command=default).grid(column=4, columnspan=2, row=5)


def alterColor(altered, colormap, btt):
    new = askcolor(color=None)
    for item in altered:
        colormap[item] = new[1]

    afile = open(r'resources//data.pkl', 'wb')
    pickle.dump(colormap, afile)
    afile.close()

    btt.config(bg=new[1])


def default():
    colormap = {']': '#a94926', '+': '#cc7832', '-': '#cc7832', '<': '#6a8759', '>': '#6a8759', ',': '#6396ba',
                '.': '#6396ba', '[': '#a94926'}

    afile = open(r'resources//data.pkl', 'wb')
    pickle.dump(colormap, afile)
    afile.close()

    messagebox.showinfo("Restart BrainIDE", "If you want to restore default colors, you will have to restart Brain IDE")
