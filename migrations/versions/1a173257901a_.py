"""empty message

Revision ID: 1a173257901a
Revises: 65691213a42f
Create Date: 2020-03-31 18:57:14.553069

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1a173257901a'
down_revision = '65691213a42f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CURRENCY',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('country', sa.String(length=32), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('EMERGENCY_CONTACT',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('firstname', sa.String(length=32), nullable=True),
    sa.Column('lastname', sa.String(length=32), nullable=True),
    sa.Column('homephone', sa.String(length=32), nullable=True),
    sa.Column('mobilephone', sa.String(length=32), nullable=True),
    sa.Column('workphone', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['USER.uuid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('TOUR_LOCATION',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tour_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('address', sa.String(length=60), nullable=True),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.uuid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('LOCATION')
    op.add_column('USER', sa.Column('dob', sa.Date(), nullable=False))
    op.add_column('USER', sa.Column('photo', sa.LargeBinary(), nullable=True))
    op.add_column('USER', sa.Column('url', sa.String(length=60), nullable=True))
    op.drop_constraint('USER_uuid_key', 'USER', type_='unique')
    op.create_unique_constraint(None, 'USER', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'USER', type_='unique')
    op.create_unique_constraint('USER_uuid_key', 'USER', ['uuid'])
    op.drop_column('USER', 'url')
    op.drop_column('USER', 'photo')
    op.drop_column('USER', 'dob')
    op.create_table('LOCATION',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"LOCATION_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('tour_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=60), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=60), autoincrement=False, nullable=True),
    sa.Column('lat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('lng', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tour_id'], ['TOUR.uuid'], name='LOCATION_tour_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='LOCATION_pkey')
    )
    op.drop_table('TOUR_LOCATION')
    op.drop_table('EMERGENCY_CONTACT')
    op.drop_table('CURRENCY')
    # ### end Alembic commands ###