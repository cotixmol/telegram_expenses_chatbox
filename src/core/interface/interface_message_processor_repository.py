from abc import ABC, abstractmethod
from core.entities import Message


class IMessageProcessorRepository(ABC):
    @abstractmethod
    def process_message(self, message: Message):
        """Identifies expense in message"""
