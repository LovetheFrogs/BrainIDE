import os
import sys

from functions import *
from config import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from pygments import lex
from pygments.lexers import BrainfuckLexer
from translator import createTranslator


window = Tk()
editor = ScrolledText(background='#2b2b2b', foreground='#808077', font=('JetBrains Mono', 13), undo=True,
                      autoseparators=True, maxundo=-1)
toCode = ScrolledText(background='#2b2b2b', foreground='#808077', font=('JetBrains Mono', 13))
output = ScrolledText(background='#2b2b2b', foreground='#808077', font=('JetBrains Mono', 13))
listBox = Listbox(window, background='#2b2b2b', foreground='white', width=35, font=('JetBrains Mono', 13))
projectDir = ''
colormap = {']': '#a94926', '+': '#cc7832', '-': '#cc7832', '<': '#6a8759', '>': '#6a8759', ',': '#6396ba',
            '.': '#6396ba', '[': '#a94926'}


def resource_path(relative_path):

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def premade(path):
    openPremade(path, window, editor, toCode, output)
    colorFormat(None)


def openTranslator():
    createTranslator(window)


def openConfig():
    createConfig(window, colormap)


def openFileAndFormat():
    openFile(window, editor, toCode, output)
    colorFormat(None)


def formatLine(line=None):
    start_range = 0
    index = editor.index('insert').split('.')

    if line is None:
        line = int(index[0])

    line_text = editor.get("{}.{}".format(line, 0), "{}.end".format(line))

    for token, content in lex(line_text, BrainfuckLexer()):
        end_range = start_range + len(content)
        keySet = content[0]
        if keySet in colormap:
            editor.tag_add(keySet, '{}.{}'.format(line, start_range), '{}.{}'.format(line, end_range))
        start_range = end_range


def colorFormat(event):
    code = editor.get('1.0', 'end-1c')
    i = 1
    for line in code.splitlines():
        editor.index("%d.0" % i)
        formatLine(line=i)
        editor.update()
        i += 1


def sideBarContents():
    listBox.delete(0, END)

    fList = os.listdir(projectDir)
    listBox.pack(fill=BOTH, side=LEFT, padx=(2.5, 1.75), pady=(2.5, 2.5))

    for item in fList:
        if item.endswith('.txt') or item.endswith('.bf'):
            listBox.insert(END, item)


def getWorkingDir():
    global projectDir

    system = resource_path('resources/system.txt')
    with open(system, 'r') as sis:
        content = sis.readlines()
    sis.close()

    if len(content) == 0:
        chooseWorkingDir()
        with open(system, 'w') as sis:
            sis.write(projectDir)
    else:
        projectDir = content[len(content) - 1]


def chooseWorkingDir():
    global projectDir
    projectDir = filedialog.askdirectory(initialdir='.//',
                                         title='Choose working directory...')
    sideBarContents()


def showContents(event):
    x = listBox.curselection()[0]

    file = projectDir + '/'
    file += listBox.get(x)

    openDialog(window, editor, file)

    colorFormat(event)


def createShorcuts():
    window.bind('<Shift-F8>', lambda x: clearAll(editor, toCode, output))
    window.bind('<Shift-F9>', lambda x: run(editor, toCode, output))
    window.bind('<Shift-F10>', lambda x: colorFormat(None))

    window.bind('<Control-Shift-A>', lambda x: save(editor))
    window.bind('<Control-Shift-S>', lambda x: saveAs(window, editor))
    window.bind('<Control-Shift-E>', lambda x: closeFile(editor))
    window.bind('<Control-Shift-O>', lambda x: chooseWorkingDir())

    window.bind('<Shift-F3>', lambda x: newFile(window, editor, toCode, output))
    window.bind('<Shift-F2>', lambda x: openFileAndFormat())


def menuBarCreator():
    menuBar = Menu(window)
    window.config(menu=menuBar)
    window.config(bg='black')

    fileMenu = Menu(menuBar, tearoff=0)
    runMenu = Menu(menuBar, tearoff=0)
    premadeMenu = Menu(menuBar, tearoff=0)

    menuBar.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label='New File...', command=lambda: newFile(window, editor, toCode, output),
                         accelerator='Shift+F3')
    fileMenu.add_command(label='Open File...', command=openFileAndFormat, accelerator='Shift+F2')
    fileMenu.add_separator()
    fileMenu.add_command(label='Save As...', command=lambda: saveAs(window, editor), accelerator='Ctrl+Shift+S')
    fileMenu.add_command(label='Save All...', command=lambda: save(editor), accelerator='Control+Shift+A')
    fileMenu.add_command(label='Close File', command=lambda: closeFile(editor), accelerator='Ctrl+Shift+E')
    fileMenu.add_separator()
    fileMenu.add_command(label='Undo', command=editor.edit_undo, accelerator='Ctrl+Z')
    fileMenu.add_command(label='Redo', command=editor.edit_redo, accelerator='Ctrl+Y')
    fileMenu.add_separator()
    fileMenu.add_command(label='Open Project...', command=chooseWorkingDir, accelerator='Control+Shift+O')
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=lambda: window.destroy(), accelerator='Alt+F4')

    menuBar.add_cascade(label='Run', menu=runMenu)
    runMenu.add_command(label='Run...', command=lambda: run(editor, toCode, output), accelerator='Shift+F9')
    runMenu.add_separator()
    runMenu.add_command(label='Format', command=lambda: colorFormat(None), accelerator='Shift+F10')
    runMenu.add_separator()
    runMenu.add_command(label='Clear Console', command=lambda: output.delete('1.0', END), accelerator='Shift+F8')

    menuBar.add_cascade(label='Premade', menu=premadeMenu)
    premadeMenu.add_command(label='Hello World!', command=lambda: premade('premade//HelloWorld.bf'))
    premadeMenu.add_command(label='Greetings!', command=lambda: premade('premade//YourName.bf'))
    premadeMenu.add_command(label='Sum', command=lambda: premade('premade//Sum.bf'))

    menuBar.add_command(label='Translator', command=openTranslator)

    menuBar.add_command(label='Config', command=openConfig)


def inicializeWindow():
    window.title('BrainIDE')

    icon = PhotoImage(file=resource_path('resources/lovethefrogs.png'))
    window.iconphoto(False, icon)
    window.geometry('800x500')

    window.config(background='#5e5e5e')

    getWorkingDir()
    sideBarContents()

    editor.pack(expand=True, fill=BOTH, padx=(1.75, 2.5), pady=(2.5, 1.75))
    editor.insert('1.0', "NOTE: ALL CHANGES MUST BE SAVED OR ELSE THEY WILL BE DELETED UPON EXITING!!")

    for c in colormap:
        editor.tag_config(c, foreground=colormap[c])

    editor.bind('<KeyRelease>', colorFormat)

    toCode.pack(expand=True, fill=BOTH, side=LEFT, padx=(1.75, 1.75), pady=(1.75, 2.5))

    output.bind("<Key>", lambda e: "break")
    output.pack(expand=True, fill=BOTH, side=RIGHT, padx=(1.75, 2.5), pady=(1.75, 2.5))

    listBox.bind("<<ListboxSelect>>", showContents)

    createShorcuts()
    menuBarCreator()
    window.mainloop()
