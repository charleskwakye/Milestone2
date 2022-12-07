"""new migration

Revision ID: 624f2810835b
Revises: 
Create Date: 2022-12-07 11:59:06.290040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '624f2810835b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'student_name',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
    )


def downgrade() -> None:
    pass
