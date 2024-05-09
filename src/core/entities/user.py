from pydantic import BaseModel


class User(BaseModel):
    id: int
    telegram_id: int
