"""initial migrate tables

Revision ID: e22097ec53a5
Revises: 4add39a02e86
Create Date: 2025-02-05 16:07:42.255609

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e22097ec53a5'
down_revision: Union[str, None] = '05d8cc13d2c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
