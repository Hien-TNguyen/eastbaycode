"""empty message

Revision ID: d26a8a051d98
Revises: bac6930a84d5
Create Date: 2018-09-15 12:04:55.322277

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd26a8a051d98'
down_revision = 'bac6930a84d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('avatar', sa.String(length=200), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(length=120), nullable=True))
    op.add_column('users', sa.Column('tokens', sa.Text(), nullable=True))
    op.drop_column('users', 'lastname')
    op.drop_column('users', 'firstname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('firstname', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('users', sa.Column('lastname', mysql.VARCHAR(length=120), nullable=True))
    op.drop_column('users', 'tokens')
    op.drop_column('users', 'name')
    op.drop_column('users', 'avatar')
    op.drop_column('users', 'active')
    # ### end Alembic commands ###
