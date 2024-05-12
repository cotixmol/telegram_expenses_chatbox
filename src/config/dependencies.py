from src.adapters.telegram_bot import PostgreSQLDatabaseRepository, MessageLLMProcessorRepository
from .config import get_database_uri


def get_message_processor_repository():
    return MessageLLMProcessorRepository()


def get_database_repository():
    database_uri = get_database_uri()
    return PostgreSQLDatabaseRepository(database_uri=database_uri)
