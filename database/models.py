from sqlalchemy import Integer, String, Numeric, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from decimal import Decimal
from database.connection import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    amount: Mapped[Decimal] = mapped_column(Numeric(18,2))
    currency: Mapped[str] = mapped_column(String(3))
    is_fraud: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    