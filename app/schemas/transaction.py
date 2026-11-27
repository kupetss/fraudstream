from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class Transaction(BaseModel):
    transaction_id: UUID = Field(default_factory=uuid4)
    user_id: int = Field(gt=0)
    amount: float = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)
