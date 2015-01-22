"""empty message

Revision ID: 503b1cce1bc1
Revises: 54a2d38c2077
Create Date: 2015-01-22 13:55:36.477662

"""

# revision identifiers, used by Alembic.
revision = '503b1cce1bc1'
down_revision = '54a2d38c2077'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('points', sa.Column('from_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('points', 'from_id')
    ### end Alembic commands ###