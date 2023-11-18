from typing import List
from pydantic import BaseModel

class ConfigAttributeBase(BaseModel):
    config_name: str
    config_value: str

class ProductVariantBase(BaseModel):
    sku: str
    sales_price: float
    purchase_price: float
    type: str
    config_attributes: List[ConfigAttributeBase]

class ProductCreate(BaseModel):
    id: int
    name: str
    uom: str
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: str
    purchase_uom: str = None
    purchase_uom_conversion_rate: float = None
    batch_tracked: bool
    variants: List[ProductVariantBase]
    additional_info: str
