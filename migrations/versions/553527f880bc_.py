"""empty message

Revision ID: 553527f880bc
Revises: 49cf70ed9564
Create Date: 2015-01-22 15:12:39.984585

"""

# revision identifiers, used by Alembic.
revision = '553527f880bc'
down_revision = '49cf70ed9564'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'created_at')
    ### end Alembic commands ###
