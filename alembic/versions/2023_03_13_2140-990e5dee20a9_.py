"""empty message

Revision ID: 990e5dee20a9
Revises: Marvin Alvarenga
Create Date: 2023-03-13 21:40:09.344325

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "990e5dee20a9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "events",
        sa.Column(
            "id", sa.Integer(), sa.Identity(always=False), nullable=False
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("total_tickets", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.CheckConstraint("total_tickets >= 0"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("events")
    # ### end Alembic commands ###
