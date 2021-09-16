"""empty message

Revision ID: e4b34b113a6a
Revises: 4fe0f80e5015
Create Date: 2021-09-16 00:21:33.668579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4b34b113a6a'
down_revision = '4fe0f80e5015'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('animal', sa.String(length=100), nullable=True),
    sa.Column('breed', sa.String(length=200), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('contact', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('liked',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.Column('liked_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('liked')
    op.drop_table('pet')
    # ### end Alembic commands ###
