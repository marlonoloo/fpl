"""Initial migration

Revision ID: d0c6ebe1cf72
Revises: 
Create Date: 2023-10-15 09:44:27.120445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0c6ebe1cf72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gameweek',
    sa.Column('gameweek_id', sa.Integer(), nullable=False),
    sa.Column('gameweek_number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('gameweek_id')
    )
    op.create_table('team',
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('team_name', sa.String(length=100), nullable=False),
    sa.Column('team_image', sa.String(length=100), nullable=True),
    sa.Column('home_difficulty', sa.Integer(), nullable=True),
    sa.Column('away_difficulty', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('team_id')
    )
    op.create_table('fixture',
    sa.Column('fixture_id', sa.Integer(), nullable=False),
    sa.Column('gameweek_id', sa.Integer(), nullable=False),
    sa.Column('home_team_id', sa.Integer(), nullable=False),
    sa.Column('away_team_id', sa.Integer(), nullable=False),
    sa.Column('fixture_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['away_team_id'], ['team.team_id'], ),
    sa.ForeignKeyConstraint(['gameweek_id'], ['gameweek.gameweek_id'], ),
    sa.ForeignKeyConstraint(['home_team_id'], ['team.team_id'], ),
    sa.PrimaryKeyConstraint('fixture_id')
    )
    op.create_table('result',
    sa.Column('result_id', sa.Integer(), nullable=False),
    sa.Column('fixture_id', sa.Integer(), nullable=False),
    sa.Column('home_team_score', sa.Integer(), nullable=False),
    sa.Column('away_team_score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fixture_id'], ['fixture.fixture_id'], ),
    sa.PrimaryKeyConstraint('result_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('result')
    op.drop_table('fixture')
    op.drop_table('team')
    op.drop_table('gameweek')
    # ### end Alembic commands ###
