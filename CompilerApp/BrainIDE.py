from CompilerApp.Interface import Interface


class BrainIDE:
    def __init__(self):
        return self

    def run(self):
        Interface.get_instance().start()
        return True


if __name__ == '__main__':
    BrainIDE.run()
