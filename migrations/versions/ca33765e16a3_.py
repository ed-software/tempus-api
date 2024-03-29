"""empty message

Revision ID: ca33765e16a3
Revises: 8e128456b7fc
Create Date: 2020-04-01 20:16:59.022809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca33765e16a3'
down_revision = '8e128456b7fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('USER', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.add_column('USER', sa.Column('location', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('USER', 'location')
    op.drop_column('USER', 'date_created')
    # ### end Alembic commands ###
