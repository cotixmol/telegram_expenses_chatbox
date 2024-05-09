from abc import ABC, abstractmethod
from core.entities import Expense, Message

class IMessageProcessor(ABC):
    @abstractmethod
    def process_message(self, message: Message):
        """Identifies expense in message"""

    def add_expense(self, expense: Expense):
        """Add an expense to the database."""
        pass