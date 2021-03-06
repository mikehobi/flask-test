"""empty message

Revision ID: 252f0ad9d013
Revises: 32bfb06d6b9a
Create Date: 2015-01-22 14:21:22.916070

"""

# revision identifiers, used by Alembic.
revision = '252f0ad9d013'
down_revision = '32bfb06d6b9a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('points', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('email', sa.String()))
    op.add_column('users', sa.Column('password', sa.String()))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    op.drop_column('points', 'user_id')
    ### end Alembic commands ###
