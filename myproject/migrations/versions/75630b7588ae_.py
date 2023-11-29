"""empty message

Revision ID: 75630b7588ae
Revises: 5fde1034598f
Create Date: 2023-11-29 16:43:04.610848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75630b7588ae'
down_revision = '5fde1034598f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fav_language', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('form', schema=None) as batch_op:
        batch_op.drop_column('fav_language')

    # ### end Alembic commands ###