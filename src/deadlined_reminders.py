from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from abc import ABC


class DeadlinedMetaReminder(Iterable):
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass
