from abc import ABC, abstractmethod
from core.entities import Expense, Message

class IDatabaseRepository(ABC):
    @abstractmethod
    def add_expense(self, expense: Expense):
        """Add an expense to the database."""
        pass