"""empty message

Revision ID: 41cddfa95837
Revises: 836d36e4e081
Create Date: 2020-05-20 20:15:59.170188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41cddfa95837'
down_revision = '836d36e4e081'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('TOUR', sa.Column('category', sa.Enum('ANIMALS', 'BEACH', 'FOODANDDRINK', 'HIKING', 'CITY', name='tourcategory'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('TOUR', 'category')
    # ### end Alembic commands ###