from abc import ABC, abstractmethod



class Engine(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def needs_service(self, milage, warning):
        pass
