"""migrate

Revision ID: 5336e4a90561
Revises: c11f3daaf900
Create Date: 2022-11-15 07:24:58.459726

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '5336e4a90561'
down_revision = 'c11f3daaf900'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('rating', sa.Integer(), nullable=False))
    op.add_column('comments', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('comments', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.drop_column('comments', 'rate')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('rate', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('comments', 'updated_at')
    op.drop_column('comments', 'created_at')
    op.drop_column('comments', 'rating')
    # ### end Alembic commands ###