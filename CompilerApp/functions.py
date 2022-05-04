from tkinter import *
from tkinter import filedialog
from brainfuck_compiler import inicialize, codeReader


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


# Have to insert a calling to the function save so it saves changes on the current file when opening a new one.
def newFile(editor, toCode, output):
    clearAll(editor, toCode, output)
    editor.insert('1.0', "NOTE: ALL CHANGES MUST BE SAVED OR ELSE THEY WILL BE DELETED UPON EXITING!!")


# Have to insert a calling to the function save so it saves changes on the current file when opening a new one.
def openFile(editor):
    editor.delete('1.0', END)
    filename = filedialog.askopenfilename(initialdir='.//',
                                          title='Open File...',
                                          filetypes=(("Brainfuck Files", '*.bf'), ("Text Files", '*.txt')))
    with open(filename, 'r') as f:
        editor.insert(INSERT, f.read())
    f.close()


def saveAs(editor):
    contents = editor.get('1.0', END)

    filename = filedialog.asksaveasfile(initialdir='.//',
                                        title="Save As...",
                                        filetypes=(("Brainfuck Files", '*.bf'), ("Text Files", '*.txt')),
                                        defaultextension='*.txt')
    f = open(filename.name, 'w')
    f.write(contents)
    f.close()
