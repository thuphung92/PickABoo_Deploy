"""empty message

Revision ID: 65abc965d248
Revises: e4b34b113a6a
Create Date: 2021-09-16 01:43:54.281599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65abc965d248'
down_revision = 'e4b34b113a6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pet', sa.Column('media', sa.String(length=200), nullable=True))
    op.drop_column('pet', 'image_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pet', sa.Column('image_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_column('pet', 'media')
    # ### end Alembic commands ###
