import os
from functions import *

window = Tk()
editor = Text(background='#0d1117', foreground='white')
toCode = Text(background='#0d1117', foreground='white')
output = Text(background='#0d1117', foreground='white')
listBox = Listbox(window, background='#0d1117', foreground='white', width=35)
projectDir = ''


def sideBarContents():
    listBox.delete(0, END)

    fList = os.listdir(projectDir)
    listBox.pack(fill=BOTH, side=LEFT)

    for item in fList:
        if item.endswith('.txt') or item.endswith('.bf'):
            listBox.insert(END, item)


def getWorkingDir():
    global projectDir

    system = './resources/system.txt'
    with open(system, 'r') as sis:
        content = sis.readlines()
    sis.close()

    if len(content) == 0:
        messagebox.showerror("Fatal Error", "System file is empty!")
    elif content[len(content) - 1] == "NONE":
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
    with open(file) as file:
        file = file.read()
    editor.delete('1.0', END)
    editor.insert(END, file)


def menuBarCreator():
    menuBar = Menu(window)
    window.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    runMenu = Menu(menuBar, tearoff=0)

    menuBar.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label='New File...', command=lambda: newFile(window, editor, toCode, output))
    fileMenu.add_command(label='Open File...', command=lambda: openFile(window, editor, toCode, output))
    fileMenu.add_separator()
    fileMenu.add_command(label='Save As...', command=lambda: saveAs(window, editor))
    fileMenu.add_command(label='Save...', command=lambda: save(editor))
    fileMenu.add_separator()
    fileMenu.add_command(label='Open Project...', command=chooseWorkingDir)
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=exit)

    menuBar.add_cascade(label='Run', menu=runMenu)
    runMenu.add_command(label='Run...', command=lambda: run(editor, toCode, output))
    runMenu.add_command(label='Clear Console', command=lambda: output.delete('1.0', END))


def inicializeWindow():
    window.title('BrainIDE')
    window.iconbitmap('.//resources//lovethefrogs.ico')

    window.config(background='#5e5e5e')

    getWorkingDir()
    sideBarContents()

    editor.pack(expand=True, fill=BOTH, padx=2.5, pady=(2.5, 1.75))

    toCode.pack(expand=True, fill=BOTH, side=LEFT, padx=(2.5, 1.75), pady=(1.75, 2.5))

    output.bind("<Key>", lambda e: "break")
    output.pack(expand=True, fill=BOTH, side=RIGHT, padx=(1.75, 2.5), pady=(1.75, 2.5))

    listBox.bind("<<ListboxSelect>>", showContents)

    menuBarCreator()
    window.mainloop()
