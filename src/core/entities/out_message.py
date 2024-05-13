from pydantic import BaseModel


class OutMessage(BaseModel):
    user_id: int
    content: str

