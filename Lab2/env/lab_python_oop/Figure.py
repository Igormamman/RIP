from abc import ABCMeta,abstractmethod


class Figure(metaclass=ABCMeta):

    @abstractmethod
    def size(self):
        pass

