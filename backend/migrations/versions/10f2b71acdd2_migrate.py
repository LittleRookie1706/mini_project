"""migrate

Revision ID: 10f2b71acdd2
Revises: 2d1e59ab55a4
Create Date: 2022-11-09 09:37:55.712363

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '10f2b71acdd2'
down_revision = '2d1e59ab55a4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'discord_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'discord_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
