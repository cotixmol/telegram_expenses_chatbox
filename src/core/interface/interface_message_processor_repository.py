from abc import ABC, abstractmethod
from src.core.entities import Message, User


class IMessageProcessorRepository(ABC):
    @abstractmethod
    def process_message(self, user: User, message: Message):
        """Identifies expense in message"""
