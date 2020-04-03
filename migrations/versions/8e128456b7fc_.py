"""empty message

Revision ID: 8e128456b7fc
Revises: 7b827f66eb2f
Create Date: 2020-04-01 20:10:32.494837

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8e128456b7fc'
down_revision = '7b827f66eb2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('REVIEWS', sa.Column('tour_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_foreign_key(None, 'REVIEWS', 'TOUR', ['tour_id'], ['uuid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'REVIEWS', type_='foreignkey')
    op.drop_column('REVIEWS', 'tour_id')
    # ### end Alembic commands ###