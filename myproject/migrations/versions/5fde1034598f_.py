"""empty message

Revision ID: 5fde1034598f
Revises: bf5d5b8d0079
Create Date: 2023-11-29 16:23:03.936351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fde1034598f'
down_revision = 'bf5d5b8d0079'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cars', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('form', schema=None) as batch_op:
        batch_op.drop_column('cars')

    # ### end Alembic commands ###
