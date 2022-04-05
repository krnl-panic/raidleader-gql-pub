"""add wow id to item

Revision ID: c3a0a1c0e08e
Revises: c5209db0c4d7
Create Date: 2022-03-26 21:53:01.873089

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c3a0a1c0e08e'
down_revision = 'c5209db0c4d7'
branch_labels = None
depends_on = None


def upgrade():
    """ """
    op.add_column('item', sa.Column('wow_id', sa.Integer, nullable=False))


def downgrade():
    """ """
    op.drop_column('item', 'wow_id')
