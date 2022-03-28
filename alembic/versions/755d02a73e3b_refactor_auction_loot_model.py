"""refactor_auction_loot_model

Revision ID: 755d02a73e3b
Revises: 8152a6203f42
Create Date: 2022-03-27 18:10:53.796693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '755d02a73e3b'
down_revision = '8152a6203f42'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('auction_session', 'winner_id')
    op.drop_column('auction_session', 'price')

    op.drop_column('auction_loot', 'loot_id')
    op.drop_column('auction_loot', 'auction_id')
    op.add_column('auction_loot', sa.Column(
        'session_id',
        sa.Integer,
        sa.ForeignKey('auction_session.id'),
          nullable=False
    ))
    op.rename_table('auction_loot', 'auction')


def downgrade():
    op.drop_column('auction', 'session_id')
    op.add_column('auction', sa.Column(
        'auction_id',
        sa.Integer,
        sa.ForeignKey('auction_session.id'),
        nullable=False
    ))
    op.add_column('auction', sa.Column(
        'loot_id',
        sa.Integer,
        sa.ForeignKey('loot.id'),
        nullable=False
    ))
    op.rename_table('auction', 'auction_loot')

    op.add_column('auction_session', sa.Column(
        'price',
        sa.Integer
    ))
    op.add_column('auction_session', sa.Column(
        'winner_id',
        sa.Integer,
        sa.ForeignKey('character.id')
    ))

