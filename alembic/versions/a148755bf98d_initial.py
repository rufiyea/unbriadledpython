"""initial

Revision ID: a148755bf98d
Revises: 
Create Date: 2023-11-18 15:32:24.206461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a148755bf98d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

print("Hii")

def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String, index=True),
        sa.Column("uom", sa.String),
        sa.Column("category_name", sa.String),
        sa.Column("is_producible", sa.Boolean),
        sa.Column("is_purchasable", sa.Boolean),
        sa.Column("type", sa.String),
        sa.Column("additional_info", sa.String),
        sa.Column("purchase_uom", sa.String, nullable=True),
        sa.Column("purchase_uom_conversion_rate", sa.Float, nullable=True),
        sa.Column("batch_tracked", sa.Boolean),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now())
    )

    op.create_table(
        "product_variants",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("sku", sa.String, unique=True, index=True),
        sa.Column("sales_price", sa.Float),
        sa.Column("purchase_price", sa.Float),
        sa.Column("type", sa.String),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id"))
    )

    op.create_table(
        "config_attributes",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("config_name", sa.String),
        sa.Column("config_value", sa.String),
        sa.Column("variant_id", sa.Integer, sa.ForeignKey("product_variants.id"))
    )


def downgrade() -> None:
    op.drop_table("config_attributes")
    op.drop_table("product_variants")
    op.drop_table("products")

