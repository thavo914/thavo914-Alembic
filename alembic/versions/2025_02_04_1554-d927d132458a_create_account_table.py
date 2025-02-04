"""create account table

Revision ID: d927d132458a
Revises: e234eedc0f1b
Create Date: 2025-02-04 15:54:30.459525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd927d132458a'
down_revision: Union[str, None] = 'e234eedc0f1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )
def downgrade() -> None:
    op.drop_table('account')

