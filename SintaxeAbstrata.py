from abc import abstractmethod
from abc import ABCMeta

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass