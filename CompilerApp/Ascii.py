from CompilerApp.Window import Window
import customtkinter as ctk
import tkinter as tk


class Ascii(Window):
    def __init__(self, name, title, window):
        super().__init__(name, title)
        self.window = tk.Toplevel(window)
        self.window.config(bg='#2b2b2b')
        self.window.title = title

        self.table = tk.PhotoImage(file='resources//ASCIITable.png').grid(row=0, columspan=5)

        self.into = ctk.CTkEntry(self.window, width=30, bg='#3b3b3b', foreground='#808077', font=('JetBrains Mono', 10))
        self.into.focus_set()
        self.into.bind('<KeyPress>', self.__enter)
        self.into.grid(column=1, row=1)

        self.labels = self.__generate_labels()

        self.output = ctk.CTkEntry(self.window, width=30, bg='#3b3b3b', foreground='#808077', font=('JetBrains Mono', 10))
        self.output.bind('<Key>', lambda e: 'break')
        self.output.grid(column=3, row=1)

        self.convert = ctk.CTkButton(self.window, text='Convert!', bg='#3b3b3b', foreground='#808077', activebackground='#2b2b2b',
                                     activeforeground='#808077', font=('JetBrains Mono', 10),
                                     command=self.__convert).grid(column=4, row=1)

    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def __convert(self):
        self.output.delete(0, 'end')
        self.output.config(foreground='#808077')
        char = self.into.get()
        if len(char) == 1:
            self.output.insert('end', ord(char))
        else:
            self.output.config(foreground='red')
            self.output.insert('end', 'ERROR')

    def __enter(self, event):
        if event.char == '\r':
            self.__convert()
        elif event.char != '':
            self.into.delete(0, 'end')

    def __generate_labels(self):
        labels = []
        labels.append(ctk.CTkLabel(self.window, text='Char', bg='#2b2b2b', foreground='#808077',
                                   font=('JetBrains Mono', 10))).grid(column=0, row=1)
        labels.append(ctk.CTkLabel(self.window, text='Value', bg='#2b2b2b', foreground='#808077',
                                   font=('JetBrains Mono', 10)).grid(column=2, row=1))

        return labels
