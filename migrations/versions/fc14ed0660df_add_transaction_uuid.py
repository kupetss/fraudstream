"""Add transaction UUID

Revision ID: fc14ed0660df
Revises: 
Create Date: 2026-11-27 15:49:44.668895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc14ed0660df'
down_revision: Union[str, Sequence[str], None] = "0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "transactions",
        sa.Column("transaction_id", sa.UUID(), nullable=True)
    )

    op.execute(
        "UPDATE transactions SET transaction_id = gen_random_uuid()"
    )

    op.alter_column(
        "transactions",
        "transaction_id",
        nullable=False
    )

    op.create_unique_constraint(
        "uq_transactions_transaction_id",
        "transactions",
        ["transaction_id"]
    )


def downgrade() -> None:
    op.drop_constraint(
        "uq_transactions_transaction_id",
        "transactions",
        type_="unique"
    )

    op.drop_column("transactions", "transaction_id")