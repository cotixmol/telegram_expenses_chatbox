from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class ExpenseCategory(Enum):
    HOUSING = "Housing"
    TRANSPORTATION = "Transportation"
    FOOD = "Food"
    UTILITIES = "Utilities"
    INSURANCE = "Insurance"
    MEDICAL_HEALTHCARE = "Medical/Healthcare"
    SAVINGS = "Savings"
    DEBT = "Debt"
    EDUCATION = "Education"
    ENTERTAINMENT = "Entertainment"
    OTHER = "Other"


class Expense(BaseModel):
    id: UUID
    user_id: int
    description: str
    amount: float
    category: ExpenseCategory
    added_at: datetime
