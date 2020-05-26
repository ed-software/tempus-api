"""empty message

Revision ID: e0a219d0af7c
Revises: d9a8a0628522
Create Date: 2020-05-20 20:38:04.079425

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e0a219d0af7c'
down_revision = 'd9a8a0628522'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('IMAGE',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=False),
    sa.Column('primary', sa.Boolean(), nullable=True),
    sa.Column('upload_date', sa.DateTime(), nullable=True),
    sa.Column('file_name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    op.drop_table('TOUR_IMAGE')
    op.add_column('TOUR', sa.Column('image', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'TOUR', 'IMAGE', ['image'], ['uuid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'TOUR', type_='foreignkey')
    op.drop_column('TOUR', 'image')
    op.create_table('TOUR_IMAGE',
    sa.Column('uuid', postgresql.UUID(), server_default=sa.text('uuid_generate_v1()'), autoincrement=False, nullable=False),
    sa.Column('tour_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('image', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.Column('primary', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.uuid'], name='TOUR_IMAGE_tour_id_fkey'),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.uuid'], name='TOUR_IMAGE_tour_id_fkey1'),
    sa.PrimaryKeyConstraint('uuid', name='TOUR_IMAGE_pkey'),
    sa.UniqueConstraint('uuid', name='TOUR_IMAGE_uuid_key')
    )
    op.drop_table('IMAGE')
    # ### end Alembic commands ###