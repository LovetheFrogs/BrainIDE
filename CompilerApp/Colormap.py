import pickle


class Colormap:
    def __init__(self, default):
        if default:
            self.colormap = {
                ']': '#a94926',
                '+': '#cc7832',
                '-': '#cc7832',
                '<': '#6a8759',
                '>': '#6a8759',
                ',': '#6396ba',
                '.': '#6396ba',
                '[': '#a94926'
            }
        else:
            self.colormap = self.__load_colormap()

    def restore_default(self):
        self.colormap = {
                ']': '#a94926',
                '+': '#cc7832',
                '-': '#cc7832',
                '<': '#6a8759',
                '>': '#6a8759',
                ',': '#6396ba',
                '.': '#6396ba',
                '[': '#a94926'
            }

    @staticmethod
    def __load_colormap(self):
        with open(r'resources//data.pkl', 'rb') as file:
            colormap = pickle.load(file)

        return colormap

    def __update_colormap(self):
        with open(r'resources//data.pkl', 'wb') as file:
            pickle.dump(self.colormap, file)
