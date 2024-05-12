from pydantic import BaseModel

class IncomingMessage(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    text: str
