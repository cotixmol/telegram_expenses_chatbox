from fastapi import FastAPI, HTTPException
from core.entities import Message, User
from core.use_cases import ProcessUserMessage
from adapters.telegram_bot import (PostgreSQLDatabaseRepository,
                                   PostgresUserRepository,
                                   MessageLLMProcessorRepository
                                   )

app = FastAPI()


@app.post("/process_message/")
async def process_message(incoming_message: Message):
    process_user_message = ProcessUserMessage(
        user_repository=PostgresUserRepository,
        message_processor_repository=MessageLLMProcessorRepository,
        database_repository=PostgreSQLDatabaseRepository)

    user = User(user_id=incoming_message.user_id)
    message = Message(content=incoming_message.text)

    try:
        response = process_user_message.execute(user=user, message=message)
        return {"status": "success", "message": response}
    except Exception as e:
        raise HTTPException(detail=str(e))
