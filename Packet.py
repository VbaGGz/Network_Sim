from random import randint


class Packet:
    __frame = [None, None, None, None, None, None, None, None, None, None]

    def __init__(self):
        for x in range(0, 10):
            if randint(1, 10000) <= 10:
                self.__frame[x] = False
            else:
                self.__frame[x] = True

    @property
    def packetErrorCheck(self):
        for x in range(0, 10):
            if not self.__frame[x]:
                return False
        return True
