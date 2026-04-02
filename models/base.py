from abc import ABC, abstractmethod
from typing import Optional


class BaseEntity(ABC):
    def __init__(self, entity_id: Optional[int], name: str):
        self._id = entity_id
        self._name = name

    @abstractmethod
    def get_info(self) -> str:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value