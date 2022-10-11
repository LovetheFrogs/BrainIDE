from CompilerApp.Window import Window


class Interface(Window):
    def __init__(self):
        raise NotImplementedError("To be implemented.")

    def get_name(self):
        raise NotImplementedError("To be implemented.")

    def start(self):
        raise NotImplementedError("To be implemented.")

    def get_instance(self):
        raise NotImplementedError("To be implemented.")

    def get_project_directory(self):
        raise NotImplementedError("To be implemented.")

    def __add_shortcuts(self):
        raise NotImplementedError("To be implemented.")

    def __show_files(self):
        raise NotImplementedError("To be implemented.")

    def __choose_working_directory(self):
        raise NotImplementedError("To be implemented.")
