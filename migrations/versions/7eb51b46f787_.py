"""empty message

Revision ID: 7eb51b46f787
Revises: 3b7a886f8ea3
Create Date: 2020-03-31 16:19:06.583892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eb51b46f787'
down_revision = '3b7a886f8ea3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'TOUR', ['uuid'])
    op.create_unique_constraint(None, 'USER', ['uuid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'USER', type_='unique')
    op.drop_constraint(None, 'TOUR', type_='unique')
    # ### end Alembic commands ###