"""add_checked_column

Revision ID: 7b5be2b5b636
Revises: 
Create Date: 2022-05-29 12:14:57.235493

"""
from wsgiref.simple_server import server_version
from xmlrpc.client import Boolean
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b5be2b5b636'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('visit', sa.Column('checked', Boolean, server_default = 'FALSE'))
    pass


def downgrade():
    pass
