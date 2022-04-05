"""rename_auction_models


Revision ID: 8152a6203f42
Revises: c3a0a1c0e08e
Create Date: 2022-03-27 18:02:03.189493

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '8152a6203f42'
down_revision = 'c3a0a1c0e08e'
branch_labels = None
depends_on = None


def upgrade():
    """ """
    op.rename_table('auction', 'auction_session')


def downgrade():
    """ """
    op.rename_table('auction_session', 'auction')
