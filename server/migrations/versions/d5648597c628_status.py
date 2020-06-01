"""status

Revision ID: d5648597c628
Revises: 6043c1f6e07f
Create Date: 2020-05-31 20:36:15.276834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5648597c628'
down_revision = '6043c1f6e07f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tms', sa.DateTime(), nullable=True),
    sa.Column('id_server', sa.Integer(), nullable=True),
    sa.Column('agent', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['id_server'], ['server.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_status_tms'), 'status', ['tms'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_status_tms'), table_name='status')
    op.drop_table('status')
    # ### end Alembic commands ###