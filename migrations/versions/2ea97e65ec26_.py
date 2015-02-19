"""empty message

Revision ID: 2ea97e65ec26
Revises: 55e951fd2d0f
Create Date: 2015-02-19 12:55:37.393939

"""

# revision identifiers, used by Alembic.
revision = '2ea97e65ec26'
down_revision = '55e951fd2d0f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_id', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'user_id')
    ### end Alembic commands ###
