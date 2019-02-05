"""empty message

Revision ID: 76760c810ec3
Revises: 12069610bf76
Create Date: 2019-01-30 22:57:54.073614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76760c810ec3'
down_revision = '12069610bf76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('hired_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('department_employee_link',
    sa.Column('department_id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('extra_data', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('department_id', 'employee_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department_employee_link')
    op.drop_table('employee')
    op.drop_table('department')
    # ### end Alembic commands ###
