"""empty message

Revision ID: 98c1b93fb4c2
Revises: 7894018a4951
Create Date: 2019-01-29 08:52:53.529636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98c1b93fb4c2'
down_revision = '7894018a4951'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'tags', ['parent_id', 'child_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tags', type_='unique')
    # ### end Alembic commands ###
