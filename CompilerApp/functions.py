from tkinter import *
from brainfuck_compiler import inicialize,codeReader

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


def newFile(editor, toCode, output):
    clearAll(editor, toCode, output)
    editor.insert('1.0', "NOTE: ALL CHANGES MUST BE SAVED OR ELSE THEY WILL BE DELETED UPON EXITING!!")

def openFile(editor, toCode, output):
    