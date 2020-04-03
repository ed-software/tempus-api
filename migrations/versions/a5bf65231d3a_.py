"""empty message

Revision ID: a5bf65231d3a
Revises: 8dfa36dddd77
Create Date: 2020-04-01 19:41:02.120214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5bf65231d3a'
down_revision = '8dfa36dddd77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('EMERGENCY_CONTACT', sa.Column('address', sa.Text(), nullable=True))
    op.alter_column('TOUR_IMAGE', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('TOUR_IMAGE', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_column('EMERGENCY_CONTACT', 'address')
    # ### end Alembic commands ###