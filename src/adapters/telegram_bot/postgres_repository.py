from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from src.core.interface import IDatabaseRepository
from src.core.entities import Expense

Base = declarative_base()


class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)


class ExpenseTable(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Numeric, nullable=False)
    category = Column(String, nullable=False)
    added_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class PostgreSQLDatabaseRepository(IDatabaseRepository):
    def __init__(self, database_uri):
        self.engine = create_engine(database_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def is_user_whitelisted(self, user_id: str) -> bool:
        with self.Session() as session:
            exists = (
                session.query(UserTable)
                .filter(UserTable.telegram_id == user_id)
                .scalar() is not None
            )
            return exists

    def add_expense(self, expense: Expense):
        with self.Session() as session:
            try:
                db_expense = ExpenseTable(
                    user_id=expense.user_id,
                    description=expense.description,
                    amount=expense.amount,
                    category=expense.category,
                    added_at=expense.add_at
                )
                session.add(db_expense)
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
