"""new fields in user model

Revision ID: 64056d2593d3
Revises: c35bba39173c
Create Date: 2022-07-21 05:44:15.784913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64056d2593d3'
down_revision = 'c35bba39173c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
