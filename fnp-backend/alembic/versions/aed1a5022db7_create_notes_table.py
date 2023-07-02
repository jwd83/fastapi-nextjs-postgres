"""create notes table

Revision ID: aed1a5022db7
Revises:
Create Date: 2023-06-27 22:50:13.418958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aed1a5022db7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String),
        sa.Column("completed", sa.Boolean)
    )

def downgrade() -> None:
    op.drop_table("notes")
