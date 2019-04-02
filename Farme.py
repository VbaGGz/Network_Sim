from random import randint


class Frame:
    __frame = None

    def __init__(self):
        if randint(1, 10000) <= 10:
            self.__frame = False
        else:
            self.__frame = True

    @property
    def get_frame(self):
        return self.__frame
