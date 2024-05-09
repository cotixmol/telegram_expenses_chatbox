from abc import ABC, abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def get_user_by_telegram_id(self, telegram_id: str):
        """Retrieve a user by their Telegram ID, return None if not found."""
        pass

    @abstractmethod
    def is_user_whitelisted(self, telegram_id: str):
        """Check if a user's Telegram ID is whitelisted."""
        pass