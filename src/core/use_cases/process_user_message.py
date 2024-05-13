from src.core.interface import IMessageProcessorRepository, IDatabaseRepository
from src.core.entities import User, Message
from src.core.exceptions import UserNotFoundException, NonRelatedToExpensesException, LLMResponseErrorException

class ProcessUserMessage:
    def __init__(self, message_processor_repository: IMessageProcessorRepository, database_repository: IDatabaseRepository):
        self.message_processor_repository = message_processor_repository
        self.database_repository = database_repository

    def execute(self, user: User, message: Message) -> str:
        if not self.database_repository.is_user_whitelisted(user.user_id):
            raise UserNotFoundException(user_id=user.user_id, first_name=user.first_name, last_name=user.last_name)

        expense = self.message_processor_repository.process_message(user, message)
        self.database_repository.add_expense(expense)
        return f"{expense.category.value} expense added✅"
