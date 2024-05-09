from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from core.interface import IDatabaseRepository
from core.entities import Expense

Base = declarative_base()


class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True, nullable=False)


class ExpenseTable(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Numeric, nullable=False)
    category = Column(String, nullable=False)
    added_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class PostgreSQLDatabaseRepository(IDatabaseRepository):
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_expense(self, expense: Expense):
        session = self.Session()
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
        finally:
            session.close()
