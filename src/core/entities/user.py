from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    telegram_id: int
