"""Add a column

Revision ID: d4808f157a34
Revises: 5f0ccb076f5f
Create Date: 2025-02-04 14:59:36.646742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4808f157a34'
down_revision: Union[str, None] = '5f0ccb076f5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade() -> None:
    op.drop_column('account', 'last_transaction_date')
