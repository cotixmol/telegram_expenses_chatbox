from core.interface import IUserRepository, IMessageProcessorRepository, IDatabaseRepository
from core.entities import User, Message


class ProcessUserMessage:
    def __init__(self,
                 user_repository: IUserRepository,
                 message_processor_repository: IMessageProcessorRepository,
                 database_repository: IDatabaseRepository):
        self.user_repository = user_repository
        self.message_processor_repository = message_processor_repository
        self.database_repository = database_repository

    def execute(self, user: User, message: Message) -> str:
        if not self.user_repository.is_user_whitelisted(user.user_id):
            raise ValueError("User not whitelisted")

        try:
            expense = self.message_processor_repository.process_message(message)
            self.database_repository.add_expense(expense)
            return f"{expense.category} expense added✅"
        except ValueError as e:
            return str(e)
