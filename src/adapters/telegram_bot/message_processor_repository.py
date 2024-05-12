from core.interface import IMessageProcessorRepository
from core.entities import Message


class MessageLLMProcessorRepository(IMessageProcessorRepository):
    def process_message(self, message: Message):
        pass