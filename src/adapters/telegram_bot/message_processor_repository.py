from openai import OpenAI
import uuid
from datetime import datetime
import json
from src.core.exceptions import NonRelatedToExpensesException, LLMResponseErrorException
from src.core.interface import IMessageProcessorRepository
from src.core.entities import Message, ExpenseCategory, User, Expense
from src.utils import validate_json_structure


class OpenAIMessageProcessorRepository(IMessageProcessorRepository):
    def __init__(self, open_ai_api_key, open_ai_model):
        self.api_key = open_ai_api_key
        self.open_ai_model = open_ai_model

    def process_message(self, user: User, message: Message) -> Expense:
        client = OpenAI(api_key=self.api_key)
        prompt = f"""
        Based on the message below, output the expense details in JSON format, choosing the appropriate category from the list:
        Food, Housing, Transportation, Utilities, Insurance, Healthcare, Savings, Debt, Education, Entertainment, Other.
        If the message does not detail an expense, respond with: {{ "error": "no expense detailed" }}
        Message: "{message.text}"
        For Example:
        Message: "I just paid $1200 for this month's rent."
        {{"description": "monthly rent", "amount": 1200, "category": "Housing"}}
        """

        response = client.chat.completions.create(
            model=self.open_ai_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60
        )

        open_ai_answer = response.choices[0].message.content

        if validate_json_structure(open_ai_answer):
            result = json.loads(response.choices[0].message.content)

            if 'error' in result:
                raise NonRelatedToExpensesException()

            category = result['category'].lower()
            category_map = {
                "food": ExpenseCategory.FOOD,
                "housing": ExpenseCategory.HOUSING,
                "transportation": ExpenseCategory.TRANSPORTATION,
                "utilities": ExpenseCategory.UTILITIES,
                "insurance": ExpenseCategory.INSURANCE,
                "medical": ExpenseCategory.MEDICAL_HEALTHCARE,
                "savings": ExpenseCategory.SAVINGS,
                "debt": ExpenseCategory.DEBT,
                "education": ExpenseCategory.EDUCATION,
                "entertainment": ExpenseCategory.ENTERTAINMENT,
                "other": ExpenseCategory.OTHER
            }

            expense_category = category_map.get(category, ExpenseCategory.OTHER).value

            expense = Expense(
                id=str(uuid.uuid4()),
                user_id=user.user_id,
                description=result['description'],
                amount=float(result['amount']),
                category=expense_category,
                added_at=datetime.now()
            )
            return expense
        else:
            raise LLMResponseErrorException()
