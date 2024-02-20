from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id

    @abstractmethod
    def validate(self):
        pass
