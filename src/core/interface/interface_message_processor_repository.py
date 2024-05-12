from abc import ABC, abstractmethod
from src.core.entities import Message


class IMessageProcessorRepository(ABC):
    @abstractmethod
    def process_message(self, message: Message):
        """Identifies expense in message"""
