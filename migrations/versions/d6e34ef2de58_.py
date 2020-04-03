"""empty message

Revision ID: d6e34ef2de58
Revises: 4c56929a47a3
Create Date: 2020-04-03 13:30:34.364186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6e34ef2de58'
down_revision = '4c56929a47a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('USER', sa.Column('customer_rating_count', sa.Integer(), nullable=True))
    op.add_column('USER', sa.Column('guide_rating_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('USER', 'guide_rating_count')
    op.drop_column('USER', 'customer_rating_count')
    # ### end Alembic commands ###