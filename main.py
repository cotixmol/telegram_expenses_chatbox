from fastapi import FastAPI, HTTPException, Depends
from dotenv import load_dotenv
from src.config import get_message_processor_repository, get_database_repository, get_user_repository
from src.core.interface import IDatabaseRepository, IMessageProcessorRepository, IUserRepository
from core.entities import Message, User
from core.use_cases import ProcessUserMessage
from adapters.telegram_bot import (PostgreSQLDatabaseRepository,
                                   PostgresUserRepository,
                                   MessageLLMProcessorRepository
                                   )

load_dotenv()

app = FastAPI()


@app.post("/process_message/")
async def process_message(
    incoming_message: Message,
    user_repository: IUserRepository = Depends(get_user_repository),
    message_processor_repository: IMessageProcessorRepository = Depends(get_message_processor_repository),
    database_repository: IDatabaseRepository = Depends(get_database_repository)
):
    process_user_message = ProcessUserMessage(
        user_repository=user_repository,
        message_processor_repository=message_processor_repository,
        database_repository=database_repository
    )

    user = User(user_id=incoming_message.user_id)
    message = Message(content=incoming_message.text)

    try:
        response = process_user_message.execute(user=user, message=message)
        return {"status": "success", "message": response}
    except Exception as e:
        raise HTTPException(detail=str(e))
