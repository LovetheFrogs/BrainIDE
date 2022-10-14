import tkinter as tk


class Menu:
    def __init__(self, window):
        self.menu_bar = tk.Menu(window)
        self.submenus = []
        self.__generate_tabs

    @abstractmethod
    def __generate_tabs(self):
        pass
