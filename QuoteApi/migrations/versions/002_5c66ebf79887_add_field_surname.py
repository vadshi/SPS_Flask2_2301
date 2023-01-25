"""add field surname

Revision ID: 5c66ebf79887
Revises: f6eda7049057
Create Date: 2023-01-25 13:02:21.638820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c66ebf79887'
down_revision = 'f6eda7049057'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('surname', sa.String(length=32), server_default='Ivanov', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author_model', schema=None) as batch_op:
        batch_op.drop_column('surname')

    # ### end Alembic commands ###