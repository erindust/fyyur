"""empty message

Revision ID: f99c7c998204
Revises: ec5d838c54b5
Create Date: 2021-11-16 23:05:50.788537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f99c7c998204'
down_revision = 'ec5d838c54b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'website')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###