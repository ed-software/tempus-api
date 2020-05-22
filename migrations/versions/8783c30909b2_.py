"""empty message

Revision ID: 8783c30909b2
Revises: e0a219d0af7c
Create Date: 2020-05-20 20:47:46.732246

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8783c30909b2'
down_revision = 'e0a219d0af7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'IMAGE', ['uuid'])
    op.add_column('TOUR', sa.Column('image_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.drop_constraint('TOUR_image_fkey', 'TOUR', type_='foreignkey')
    op.create_foreign_key(None, 'TOUR', 'IMAGE', ['image_id'], ['uuid'])
    op.drop_column('TOUR', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('TOUR', sa.Column('image', postgresql.UUID(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'TOUR', type_='foreignkey')
    op.create_foreign_key('TOUR_image_fkey', 'TOUR', 'IMAGE', ['image'], ['uuid'])
    op.drop_column('TOUR', 'image_id')
    op.drop_constraint(None, 'IMAGE', type_='unique')
    # ### end Alembic commands ###
