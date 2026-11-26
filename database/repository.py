from decimal import Decimal
from database.connection import session_local
from database.models import Transaction

def save_transaction(data: dict, is_fraud:bool):
    with session_local() as session:
        transaction = Transaction(
            user_id = data["user_id"],
            amount=Decimal(str(data["amount"])),
            currency=data["currency"],
            is_fraud = is_fraud
        )
        session.add(transaction)
        session.commit()