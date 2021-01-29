"""set field settings

Revision ID: 6759d11e0bdd
Revises: 35957019f7a8
Create Date: 2021-01-29 07:58:48.444177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6759d11e0bdd'
down_revision = '35957019f7a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
