from CompilerApp.Menu import Menu
from CompilerApp.Functions import Functions as f
from CompilerApp.Interface import Interface as interface
import tkinter as tk
import threading as th


class InterfaceMenu(Menu):
    def __init__(self, window):
        super().__init__(window)

    def __generate_file_menu(self, opt):
        self.submenus[opt].add_command(label='New File...', command=f.new_file,
                                       accelerator='Shift+F3')
        self.submenus[opt].add_command(label='Open File...', command=f.open_file, accelerator='Shift+F2')
        self.submenus[opt].add_separator()

        self.submenus[opt].add_command(label='Save As...', command=f.save_as, accelerator='Ctrl+Shift+S')
        self.submenus[opt].add_command(label='Save All...', command=f.save, accelerator='Control+Shift+A')
        self.submenus[opt].add_command(label='Close File', command=f.close_file, accelerator='Ctrl+Shift+E')
        self.submenus[opt].add_separator()

        self.submenus[opt].add_command(label='Undo', command=interface.editor.edit_undo, accelerator='Ctrl+Z')
        self.submenus[opt].add_command(label='Redo', command=interface.editor.edit_redo, accelerator='Ctrl+Y')
        self.submenus[opt].add_separator()

        self.submenus[opt].add_command(label='Open Project...', command=f.choose_working_dir,
                                       accelerator='Control+Shift+O')
        self.submenus[opt].add_separator()

        self.submenus[opt].add_command(label='Exit', command=interface.window.destroy, accelerator='Alt+F4')
        self.submenus[opt].add_separator()

    def __generate_run_menu(self, opt):
        self.submenus[opt].add_command(label='Run...', command=f.run, accelerator='Shift+F9')
        self.submenus[opt].add_separator()

        self.submenus[opt].add_command(label='Format', command=f.colorFormat, accelerator='Shift+F10')
        self.submenus[opt].add_separator()

        self.submenus[opt].add_command(label='Clear Console', command=lambda: interface.output.delete('1.0', END),
                                       accelerator='Shift+F8')
        self.submenus[opt].add_separator()

    def __generate_premade_menu(self, opt):
        self.submenus[opt].add_command(label='Hello World!', command=lambda: f.open_premade('premade//HelloWorld.bf'))
        self.submenus[opt].add_command(label='Greetings!', command=lambda: f.open_premade('premade//YourName.bf'))
        self.submenus[opt].add_command(label='Sum', command=lambda: f.open_premade('premade//Sum.bf'))

    def __generate_help_menu(self, opt):
        self.submenus[opt].add_command(label='BrainIDE help',
                                       command=lambda: f.open_help('https://lovethefrogs.github.io/BrainIDE/brainide-help.html'),
                                       accelerator='Shift+F1')
        self.submenus[opt].add_command(label='Brainfuck help',
                                       command=lambda: f.open_help('https://lovethefrogs.github.io/BrainIDE/brainfuck-help.html'))
        self.submenus[opt].add_command(label='Shortcuts',
                                       command=lambda: f.open_help('https://lovethefrogs.github.io/BrainIDE/shortcuts-help.html'))
        self.submenus[opt].add_command(label='Translate help',
                                       command=lambda: f.open_help('https://lovethefrogs.github.io/BrainIDE/translator-help.html'))

    def __generate_tabs(self):
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=file_menu)
        self.submenus.append(file_menu)

        run_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Run', menu=run_menu)
        self.submenus.append(run_menu)

        premade_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Premade', menu=premade_menu)
        self.submenus.append(premade_menu)

        self.menu_bar.add_command(label='Translator', command=f.open_translator)

        self.menu_bar.add_command(label='ASCII', command=f.open_ascii)

        self.menu_bar.add_command(label='Config Colors', command=f.open_config)

        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Help', menu=help_menu)
        self.submenus.append(help_menu)

        t1 = th.Thread(target=self.__generate_file_menu(0))
        t2 = th.Thread(target=self.__generate_run_menu(1))
        t3 = th.Thread(target=self.__generate_premade_menu(2))
        t4 = th.Thread(target=self.__generate_help_menu(3))

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()