from src.core.interface import IMessageProcessorRepository
from src.core.entities import Message


class MessageLLMProcessorRepository(IMessageProcessorRepository):
    def process_message(self, message: Message):
        print("MessageLLMProcessorRepository")
