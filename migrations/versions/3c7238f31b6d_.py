"""empty message

Revision ID: 3c7238f31b6d
Revises: d6e34ef2de58
Create Date: 2020-05-12 17:24:42.590450

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3c7238f31b6d'
down_revision = 'd6e34ef2de58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TOUR_IMAGE',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('tour_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=False),
    sa.Column('primary', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.uuid'], ),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('primary', 'tour_id', name='primary_image_constraint'),
    sa.UniqueConstraint('uuid')
    )
    op.drop_column('TOUR', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('TOUR', sa.Column('category', postgresql.ARRAY(postgresql.ENUM('ANIMALS', 'BEACH', 'FOODANDDRINK', 'HIKING', 'CITY', name='tourcategory')), autoincrement=False, nullable=False))
    op.drop_table('TOUR_IMAGE')
    # ### end Alembic commands ###