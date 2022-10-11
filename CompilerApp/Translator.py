from CompilerApp.Window import Window


class Translator(Window):
    def __init__(self):
        raise NotImplementedError("To be implemented.")

    def get_name(self):
        raise NotImplementedError("To be implemented.")

    def translate(self):
        raise NotImplementedError("To be implemented.")

    def __translate_first(self):
        raise NotImplementedError("To be implemented.")

    def __translate_rest(self):
        raise NotImplementedError("To be implemented.")
