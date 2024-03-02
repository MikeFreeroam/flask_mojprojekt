"""Create users table

Revision ID: 6e6e33fafa68
Revises: 
Create Date: 2024-03-02 16:52:32.101927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e6e33fafa68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
             "user",
             sa.Column("id", sa.Integer, primary_key=True),
             sa.Column("username", sa.String),
             sa.Column("password", sa.String))


def downgrade():
    op.drop_table("user")
