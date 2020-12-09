# -*- encoding: utf8 -*-


class TTarget:
    def __init__(self, name, state, position=None):
        self.__name = name
        self.__state = state
        self.__position = position

    def __str__(self):
        return "Target: {} {} {}".format(self.__name, self.__state, "" if not self.__position else self.__position)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
