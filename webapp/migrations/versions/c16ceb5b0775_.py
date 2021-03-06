"""empty message

Revision ID: c16ceb5b0775
Revises: d26a8a051d98
Create Date: 2018-09-16 23:20:55.245610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c16ceb5b0775'
down_revision = 'd26a8a051d98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('startdate', sa.Date(), nullable=True),
    sa.Column('enddate', sa.Date(), nullable=True),
    sa.Column('semester', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['professor_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('startdate', sa.Date(), nullable=True),
    sa.Column('enddate', sa.Date(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('registrations',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], )
    )
    op.create_table('assignments_problems',
    sa.Column('assignment_id', sa.Integer(), nullable=True),
    sa.Column('problem_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assignment_id'], ['assignments.id'], ),
    sa.ForeignKeyConstraint(['problem_id'], ['problems.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assignments_problems')
    op.drop_table('registrations')
    op.drop_table('assignments')
    op.drop_table('courses')
    # ### end Alembic commands ###
