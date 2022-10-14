import sys
import os
from CompilerApp.Colormap import Colormap
from CompilerApp.Compiler import Compiler
from CompilerApp.InterfaceMenu import InterfaceMenu
from CompilerApp.Window import Window
from CompilerApp.Functions import Functions as func
import customtkinter as ctk
import tkinter as tk


class Interface(Window):
    def __init__(self, name, title):
        super().__init__(name, title)
        self.window = ctk.CTk()
        self.instance = None
        self.icon = tk.PhotoImage(file=self.__resource_path('resources/lovethefrogs.png'))
        self.editor = ctk.Text(root=self.window, font=('JetBrains Mono', 13), undo=True,
                               autoseparators=True, maxundo=-1)
        self.into = ctk.Text(root=self.window, font=('JetBrains Mono', 13), undo=True,
                             autoseparators=True, maxundo=-1)
        self.output = ctk.Text(root=self.window, font=('JetBrains Mono', 13), undo=True,
                               autoseparators=True, maxundo=-1)
        self.file_list = ctk.Listbox(root=self.window, width=35, font=('JetBrains Mono', 13))
        self.project_directory = ""
        self.colormap = Colormap(default=False)
        self.menu = InterfaceMenu()
        self.shortcuts = {}
        self.compiler = Compiler()

        self.__create_window()
        self.__add_shortcuts()

    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    # Add this method to UML later.
    @staticmethod
    def __resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def start(self):
        self.window.mainloop()

    def get_instance(self):
        if self.instance is None:
            self.instance = Interface("Main_Interface", "BrainIDE")

        return self.instance

    def get_project_directory(self):
        with open(self.__resource_path('resources/system.txt'), 'r') as file:
            content = file.readlines()

        if len(content) == 0:
            self.__choose_working_directory()
        else:
            self.project_directory = content[len(content) - 1]

    def __create_window(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        self.window.title(self.get_title())
        self.window.iconphoto(False, self.icon)
        self.window.geometry('800x500')

        self.get_project_directory()
        self.__sidebar_contents()

        self.editor.pack(expand=True, fill=tk.BOTH, padx=(1.75, 2.5), pady=(2.5, 1.75))
        self.editor.insert('1.0', "NOTE: ALL CHANGES MUST BE SAVED OR ELSE THEY WILL BE DELETED UPON EXITING!!")
        self.editor.bind('<KeyRelease>', func.color_format())

        self.into.pack(expand=True, fill=tk.BOTH, side=tk.LEFT, padx=(1.75, 1.75), pady=(1.75, 2.5))

        self.output.bind("<Key>", lambda e: "break")
        self.output.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT, padx=(1.75, 2.5), pady=(1.75, 2.5))

        self.file_list.bind("<<ListboxSelect>>", func.sidebar_show_contents())

        # window.config(background='#5e5e5e')

    def __add_shortcuts(self):
        self.window.bind('<Shift-F8>', func.clear_all)
        self.window.bind('<Shift-F9>', func.run)
        self.window.bind('<Shift-F10>', func.color_format)

        self.window.bind('<Control-Shift-A>', func.save)
        self.window.bind('<Control-Shift-S>', func.save_as())
        self.window.bind('<Control-Shift-E>', func.close_file())
        self.window.bind('<Control-Shift-O>', self.__choose_working_directory())

        self.window.bind('<Shift-F1>', func.open_help('https://lovethefrogs.github.io/BrainIDE/brainide-help.html'))
        self.window.bind('<Shift-F3>', func.new_file)
        self.window.bind('<Shift-F2>', func.open_file)

    def __show_files(self, event):
        x = self.file_list.curselection()[0]

        file = self.project_directory + '/'
        file += self.file_list.get(x)

        func.open_file()

    def __choose_working_directory(self):
        self.project_directory = ctk.filedialog.askdirectory(initialdir='.//',
                                                             title='Choose working directory...')
        func.sidebar_show_contents()
