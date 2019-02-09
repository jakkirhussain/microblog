"""empty message

Revision ID: 582e6fd0f3a0
Revises: 75407c9d5eaa
Create Date: 2019-02-09 12:57:58.919017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '582e6fd0f3a0'
down_revision = '75407c9d5eaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image_file', sa.String(length=64), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'image_file')
    # ### end Alembic commands ###
