"""empty message

Revision ID: 7d9428c9eb84
Revises: 1da7a2dc7463
Create Date: 2020-04-01 14:19:16.598922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d9428c9eb84'
down_revision = '1da7a2dc7463'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('TOUR', sa.Column('category', sa.Enum('ANIMALS', 'BEACH', 'HIKING', 'FOOD AND DRINK', 'CITY'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('TOUR', 'category')
    # ### end Alembic commands ###
