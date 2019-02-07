"""empty message

Revision ID: 1dc5d9b3886e
Revises: ccac6db519ad
Create Date: 2019-02-05 22:08:49.930922

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1dc5d9b3886e'
down_revision = 'ccac6db519ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('skills', 'percent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('skills', sa.Column('percent', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
