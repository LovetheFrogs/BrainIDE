from CompilerApp.Menu import Menu
import tkinter as tk
from CompilerApp.Translator import Translator as tt


class TranslatorMenu(Menu):
    def __init__(self, window):
        super().__init__(window)
        self.__generate_tabs()

    def __generate_tabs(self):
        translate_opt = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Translator', menu=translate_opt)
        self.submenus.append(translate_opt)

        translate_opt.add_command(label='Translate!', command=tt.translate,
                                  accelerator='Shift+F12')
        translate_opt.add_command(label='Copy Output', command=tt.copy_output,
                                  accelerator='Ctrl+Shift+C')
