"""added about and lastseen

Revision ID: ba3024701169
Revises: a597cf7bae3b
Create Date: 2020-05-17 21:16:51.193064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba3024701169'
down_revision = 'a597cf7bae3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about', sa.String(length=240), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_about'), 'user', ['about'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_about'), table_name='user')
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about')
    # ### end Alembic commands ###