from fastapi import FastAPI, Depends, status
from dotenv import load_dotenv
from src.config import get_message_processor_repository, get_database_repository
from src.core.interface import IDatabaseRepository, IMessageProcessorRepository
from src.core.entities import Message, User, IncomingMessage
from src.core.use_cases import ProcessUserMessage
from src.utils import standard_response
from src.core.exceptions import UserNotFoundException, NonRelatedToExpensesException, LLMResponseErrorException

load_dotenv()

application = FastAPI()


@application.post("/process_message/")
async def process_message(
    incoming_message: IncomingMessage,
    message_processor_repository: IMessageProcessorRepository = Depends(get_message_processor_repository),
    database_repository: IDatabaseRepository = Depends(get_database_repository)
):
    process_user_message = ProcessUserMessage(
        message_processor_repository=message_processor_repository,
        database_repository=database_repository
    )

    user = User(
        user_id=incoming_message.user_id,
        first_name=incoming_message.first_name,
        last_name=incoming_message.last_name
    )
    message = Message(text=incoming_message.text)

    try:
        response = process_user_message.execute(user=user, message=message)
        return standard_response(status_code=status.HTTP_200_OK, message={"user_id": user.user_id, "content": response})
    except UserNotFoundException as e:
        return standard_response(status_code=e.status_code, message={"user_id": user.user_id, "content": e.detail})
    except NonRelatedToExpensesException as e:
        return standard_response(status_code=e.status_code, message={"user_id": user.user_id, "content": e.detail})
    except LLMResponseErrorException as e:
        return standard_response(status_code=e.status_code, message={"user_id": user.user_id, "content": e.detail})
    except Exception as e:
        return standard_response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message={"user_id": user.user_id, "content": "An unexpected error occurred"})