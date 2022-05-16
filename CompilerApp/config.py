from tkinter import *
from tkinter.colorchooser import askcolor


def createConfig(window, colormap):
    config = Toplevel(window)
    config.title('BrainIDE - Config')
    config.config(bg='black')

    Label(config, text='THIS IS CURRENTLY BEING WORKED ON', background='#2b2b2b', foreground='#808077').pack()

    '''Label(config, background='#2b2b2b', foreground='#808077', text="Change your symbols colors.",
          font=('JetBrains Mono', 20)).pack(side=TOP, fill=BOTH)
    Button(config, text="Brackets ([ and ])", font=('JetBrains Mono', 20),
           command=lambda: coloring(0, colormap)).pack(side=TOP)


def coloring(opt, colormap):
    color = askcolor(title='Select a color...')
    if opt == 1:
        colormap['['] = color[1]
        colormap[']'] = color[1]'''
