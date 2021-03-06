"""empty message

Revision ID: 718f66fa54b1
Revises: 8b456af3cd6d
Create Date: 2020-07-05 13:13:52.680284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '718f66fa54b1'
down_revision = '8b456af3cd6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('capital', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'capital', 'loan', ['loan_id'], ['id'])
    op.create_foreign_key(None, 'capital', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'loan', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'userbill', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'userfund', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'userfund', type_='foreignkey')
    op.drop_constraint(None, 'userbill', type_='foreignkey')
    op.drop_constraint(None, 'loan', type_='foreignkey')
    op.drop_constraint(None, 'capital', type_='foreignkey')
    op.drop_constraint(None, 'capital', type_='foreignkey')
    op.drop_column('capital', 'user_id')
    # ### end Alembic commands ###
