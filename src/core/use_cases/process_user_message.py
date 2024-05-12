from src.core.interface import IMessageProcessorRepository, IDatabaseRepository
from src.core.entities import User, Message


class ProcessUserMessage:
    def __init__(self,
                 message_processor_repository: IMessageProcessorRepository,
                 database_repository: IDatabaseRepository):
        self.message_processor_repository = message_processor_repository
        self.database_repository = database_repository

    def execute(self, user: User, message: Message) -> str:
        if not self.database_repository.is_user_whitelisted(user.user_id):
            raise ValueError("User not whitelisted")

        try:
            expense = self.message_processor_repository.process_message(message)
            self.database_repository.add_expense(expense)
            return f"{expense.category} expense added✅"
        except ValueError as e:
            return str(e)
