from core.interface import IUserRepository, IMessageProcessor
from core.entities import User, Message, Exp

class ProcessUserMessage:
    def __init__(self, user_repository: IUserRepository, message_processor: IMessageProcessor):
        self.user_repo = user_repository 
        self.message_processor = message_processor

    def execute(self, user: User, message: Message) -> str:
        if not self.user_repo.is_user_whitelisted(user.user_id):
            raise ValueError("User not whitelisted")

        try:
            expense = self.message_processor.process_message(message)
            self.message_processor.add_expense(expense) 
            return f"{expense.category} expense added✅"
        except ValueError as e:
            return str(e)
