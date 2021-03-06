"""empty message

Revision ID: 49cf70ed9564
Revises: d85f18676b1
Create Date: 2015-01-22 14:26:33.691642

"""

# revision identifiers, used by Alembic.
revision = '49cf70ed9564'
down_revision = 'd85f18676b1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
