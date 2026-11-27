import logging
from decimal import Decimal
from database.connection import session_local
from database.models import Transaction
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import insert
from uuid import UUID

def save_transaction(data: dict, is_fraud:bool) -> bool:
    with session_local() as session:
        try:
            statement = insert(Transaction).values(
                transaction_id = UUID(data["transaction_id"]),
                user_id = data["user_id"],
                amount=Decimal(str(data["amount"])),
                currency=data["currency"],
                is_fraud = is_fraud
            )
            statement = statement.on_conflict_do_nothing(index_elements=["transaction_id"]).returning(Transaction.id)
            result = session.execute(statement)
            insert_id = result.scalar_one_or_none()
            session.commit()
            if insert_id is None:
                logging.info("Duplicate transaction skipped")
                return False
            
            return True

        except SQLAlchemyError:
            session.rollback()
            logging.exception("Failed to save transaction")
            raise