from abc import ABC, abstractmethod


class Command(ABC):
    """命令接口"""

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def is_undoable(self) -> bool:
        """是否可撤销"""
        pass


