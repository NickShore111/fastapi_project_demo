"""add foreign-key to posts table

Revision ID: 50427c177046
Revises: 407d662ac548
Create Date: 2022-01-08 13:19:42.113089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50427c177046'
down_revision = '407d662ac548'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
