"""empty message

Revision ID: 96bf587c2551
Revises: 8b71c431ef53
Create Date: 2022-11-28 19:47:53.170294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96bf587c2551'
down_revision = '8b71c431ef53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('report_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'item', 'report', ['report_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.drop_column('item', 'report_id')
    # ### end Alembic commands ###