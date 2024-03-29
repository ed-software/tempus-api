"""empty message

Revision ID: 2a78abfc1c9f
Revises: ca33765e16a3
Create Date: 2020-04-02 13:24:05.828125

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2a78abfc1c9f'
down_revision = 'ca33765e16a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('USER_X_LANGUAGE',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language_id', sa.String(length=5), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['language_id'], ['LANGUAGE.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['USER.uuid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('VERNACULAR')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('VERNACULAR',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"VERNACULAR_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('language_id', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
    sa.Column('user_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['language_id'], ['LANGUAGE.id'], name='VERNACULAR_language_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['USER.uuid'], name='VERNACULAR_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='VERNACULAR_pkey')
    )
    op.drop_table('USER_X_LANGUAGE')
    # ### end Alembic commands ###
