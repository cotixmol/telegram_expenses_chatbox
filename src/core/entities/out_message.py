from pydantic import BaseModel


class OutMessage(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    content: str

