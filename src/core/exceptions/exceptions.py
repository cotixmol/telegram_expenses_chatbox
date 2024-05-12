from fastapi import status


class UserNotFoundException(Exception):
    def __init__(self, user_id: int, first_name: str, last_name: str):
        self.detail = f"User {first_name} {last_name} with telegram ID {user_id} not whitelisted. Usage is forbidden"
        self.status_code = status.HTTP_403_FORBIDDEN
