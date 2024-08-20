"""empty message

Revision ID: 857f94704f96
Revises: 08079adfcbcb
Create Date: 2024-08-20 11:39:38.619286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '857f94704f96'
down_revision = '08079adfcbcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###