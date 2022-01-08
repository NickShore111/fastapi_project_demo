"""add content column to posts table

Revision ID: 93b6bb579fc4
Revises: 89a5c9d535b7
Create Date: 2022-01-08 12:34:15.350168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93b6bb579fc4'
down_revision = '89a5c9d535b7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
