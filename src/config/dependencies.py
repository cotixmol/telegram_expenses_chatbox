from src.adapters.telegram_bot import PostgreSQLDatabaseRepository, MessageLLMProcessorRepository, PostgresUserRepository
from .config import get_database_uri 

def get_user_repository():
    return PostgresUserRepository()

def get_message_processor_repository():
    return MessageLLMProcessorRepository()

def get_database_repository():
    database_uri = get_database_uri()
    return PostgreSQLDatabaseRepository(database_uri)
