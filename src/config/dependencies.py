from src.adapters.telegram_bot import PostgreSQLDatabaseRepository, OpenAIMessageProcessorRepository
from .config import get_database_uri, get_open_ai_api_key, get_open_ai_model


def get_message_processor_repository():
    open_ai_api_key = get_open_ai_api_key()
    open_ai_model = get_open_ai_model()
    return OpenAIMessageProcessorRepository(open_ai_api_key=open_ai_api_key, open_ai_model=open_ai_model)


def get_database_repository():
    database_uri = get_database_uri()
    return PostgreSQLDatabaseRepository(database_uri=database_uri)
