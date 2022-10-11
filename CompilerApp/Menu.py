import customtkinter as ctk


class Menu:
    def __init__(self, window):
        self.menu_bar = ctk.Menu(window)
        self.submenus = []

    @abstractmethod
    def __generate_tabs(self):
        pass
