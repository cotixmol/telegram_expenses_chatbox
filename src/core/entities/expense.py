from pydantic import BaseModel
from datetime import datetime

class Expense(BaseModel):
    id: int
    user_id: int
    description: str
    amount: float
    category: str
    add_at: datetime


