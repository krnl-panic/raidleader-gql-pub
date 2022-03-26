"""create raid table

Revision ID: ba7157cdd6ea
Revises: 
Create Date: 2022-03-26 04:15:32.784750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba7157cdd6ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'raid',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(128), nullable=False),
        sa.Column('start_time', sa.DateTime(timezone=True)),
        sa.Column('end_time', sa.DateTime(timezone=True)),
        sa.Column('created_at', sa.DateTime(timezone=True)),
        sa.Column('updated_at', sa.DateTime(timezone=True)),
        sa.Column('deleted_at', sa.DateTime(timezone=True)),
    )


def downgrade():
    op.drop_table('raid')
