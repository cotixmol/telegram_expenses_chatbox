from fastapi import status, Request
from src.utils import standard_response


class UserNotFoundException(Exception):
    def __init__(self, user_id: int, first_name: str, last_name: str):
        self.detail = f"User {first_name} {last_name} with telegram ID {user_id} not whitelisted. Usage is forbidden"
        self.status_code = status.HTTP_403_FORBIDDEN


class NonRelatedToExpensesException(Exception):
    def __init__(self, user_id: int,):
        self.detail = "Sorry, but your message is not related to expenses. Try in a different or more direct way,"
        self.status_code = status.HTTP_400_BAD_REQUEST


class LLMResponseErrorException(Exception):
    def __init__(self, user_id: int,):
        self.detail = "There was a problem with the request. Please send you message again."
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR