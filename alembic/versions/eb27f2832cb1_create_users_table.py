"""create users table

Revision ID: eb27f2832cb1
Revises: 
Create Date: 2023-03-02 14:44:24.479389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb27f2832cb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('username', sa.String(), nullable=True), sa.Column('email', sa.String(), nullable=True), sa.Column('password', sa.String(), nullable=True), sa.PrimaryKeyConstraint('id', name=op.f('users_pkey')))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_pkey', 'users', type_='primary')
    op.drop_table('users')
    # ### end Alembic commands ###