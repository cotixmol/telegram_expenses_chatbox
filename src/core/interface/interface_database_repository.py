from abc import ABC, abstractmethod
from src.core.entities import Expense


class IDatabaseRepository(ABC):
    @abstractmethod
    def is_user_whitelisted(self, telegram_id: str):
        """Check if a user's Telegram ID is whitelisted."""
        pass

    @abstractmethod
    def add_expense(self, expense: Expense):
        """Add an expense to the database."""
        pass
