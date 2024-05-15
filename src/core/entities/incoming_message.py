from typing import Optional
from pydantic import BaseModel


class IncomingMessage(BaseModel):
    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    text: str
