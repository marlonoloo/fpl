"""Remove fixture_date and add expected goals columns

Revision ID: ea4c4ad61ebf
Revises: d0c6ebe1cf72
Create Date: 2023-10-16 13:55:12.456075

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ea4c4ad61ebf'
down_revision = 'd0c6ebe1cf72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fixture', schema=None) as batch_op:
        batch_op.drop_column('fixture_date')

    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.add_column(sa.Column('xg', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('xg_conceded', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.drop_column('xg_conceded')
        batch_op.drop_column('xg')

    with op.batch_alter_table('fixture', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fixture_date', mysql.DATETIME(), nullable=False))

    # ### end Alembic commands ###