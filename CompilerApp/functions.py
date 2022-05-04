from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from brainfuck_compiler import inicialize, codeReader

currWorkDir = None


def clearAll(editor, toCode, output):
    output.delete('1.0', END)
    toCode.delete('1.0', END)
    editor.delete('1.0', END)


def run(editor, toCode, output):
    output.delete('1.0', END)
    lang, pointer = inicialize()
    code = editor.get('1.0', 'end-1c')
    input_data = toCode.get('1.0', END).strip()

    result = codeReader(lang, code, pointer, input_data)

    output.insert(END, result + '\n')


def newFile(window, editor, toCode, output):
    if currWorkDir is not None:
        save(editor)

    clearAll(editor, toCode, output)
    editor.insert('1.0', "NOTE: ALL CHANGES MUST BE SAVED OR ELSE THEY WILL BE DELETED UPON EXITING!!")

    window.title("New File... - BrainIDE [UNSAVED]")


def openFile(window, editor, toCode, output):
    global currWorkDir
    if currWorkDir is not None:
        save(editor)

    clearAll(editor, toCode, output)
    filename = filedialog.askopenfilename(initialdir='.//',
                                          title='Open File...',
                                          filetypes=(("Brainfuck Files", '*.bf'), ("Text Files", '*.txt')))

    currWorkDir = filename

    with open(filename, 'r') as f:
        editor.insert(INSERT, f.read())
    f.close()
    window.title(f'{filename} - BrainIDE')


def saveAs(window, editor):
    contents = editor.get('1.0', END)

    filename = filedialog.asksaveasfile(initialdir='.//',
                                        title="Save As...",
                                        filetypes=(("Brainfuck Files", '*.bf'), ("Text Files", '*.txt')),
                                        defaultextension='*.txt')

    global currWorkDir
    currWorkDir = filename.name

    f = open(currWorkDir, 'w')
    f.write(contents)
    f.close()

    window.title(f'{filename.name} - BrainIDE')


def save(editor):
    global currWorkDir
    if currWorkDir is None:
        messagebox.showerror("File Error", "Error: Can not save a file wich is not existing. Open an existing file or "
                                           "Save As first.")
    else:
        contents = editor.get('1.0', END)

        f = open(currWorkDir, 'w')
        f.write(contents)
