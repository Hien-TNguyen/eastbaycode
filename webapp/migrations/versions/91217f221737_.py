"""empty message

Revision ID: 91217f221737
Revises: f61efa4ad631
Create Date: 2018-09-14 14:54:10.593067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91217f221737'
down_revision = 'f61efa4ad631'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assignments', sa.Column('grade', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assignments', 'grade')
    # ### end Alembic commands ###
