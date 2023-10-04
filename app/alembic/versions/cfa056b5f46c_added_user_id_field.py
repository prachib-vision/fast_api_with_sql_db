"""added user_id field

Revision ID: cfa056b5f46c
Revises: 8c9a51bc2e16
Create Date: 2023-10-02 15:16:12.271601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cfa056b5f46c'
down_revision: Union[str, None] = '8c9a51bc2e16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_id')
    # ### end Alembic commands ###
