"""renaming column name to full_name

Revision ID: 79429c385d9f
Revises: 791279dd0760
Create Date: 2026-02-01 17:31:41.590551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79429c385d9f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='full_name')


def downgrade() -> None:
    op.alter_column('students', 'full_name', new_column_name='name')
