"""empty message

Revision ID: f606d577f363
Revises: 1e13fedcf647
Create Date: 2019-01-29 01:10:59.283139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f606d577f363'
down_revision = '1e13fedcf647'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('section', sa.String(length=100), nullable=False),
    sa.Column('question_content', sa.String(length=500), nullable=False),
    sa.Column('a', sa.String(length=100), nullable=False),
    sa.Column('b', sa.String(length=100), nullable=False),
    sa.Column('c', sa.String(length=100), nullable=False),
    sa.Column('d', sa.String(length=100), nullable=False),
    sa.Column('ans', sa.String(length=100), nullable=False),
    sa.Column('positive_marks', sa.Integer(), nullable=False),
    sa.Column('negative_marks', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test_name', sa.String(length=50), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('instructions', sa.String(length=1000), nullable=False),
    sa.Column('no_of_questions', sa.Integer(), nullable=False),
    sa.Column('total_marks', sa.Integer(), nullable=False),
    sa.Column('time_in_mins', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(timezone=True), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['test_id'], ['test.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_score', sa.Integer(), nullable=False),
    sa.Column('positive_score', sa.Integer(), nullable=False),
    sa.Column('negative_score', sa.Integer(), nullable=False),
    sa.Column('correct_answers', sa.Integer(), nullable=False),
    sa.Column('wrong_answers', sa.Integer(), nullable=False),
    sa.Column('no_answers', sa.Integer(), nullable=False),
    sa.Column('attempted_ques', sa.Integer(), nullable=False),
    sa.Column('test_taken_on_date', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['test_id'], ['test.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('test_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_test')
    op.drop_table('test_question')
    op.drop_table('test')
    op.drop_table('question')
    # ### end Alembic commands ###
