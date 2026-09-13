from abc import ABC, abstractmethod
from typing import Optional


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Optional[object] = None) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
