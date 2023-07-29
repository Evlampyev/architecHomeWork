from abc import ABC, abstractmethod


class IPrinter(ABC):

    @abstractmethod
    def printT(self, data):
        pass
