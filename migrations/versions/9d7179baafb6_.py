"""empty message

Revision ID: 9d7179baafb6
Revises: 8783c30909b2
Create Date: 2020-05-20 20:59:42.671612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d7179baafb6'
down_revision = '8783c30909b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('IMAGE', 'primary')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('IMAGE', sa.Column('primary', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
