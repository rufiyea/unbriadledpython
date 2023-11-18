from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    uom = Column(String)
    category_name = Column(String)
    is_producible = Column(Boolean)
    is_purchasable = Column(Boolean)
    type = Column(String)
    additional_info = Column(String)
    purchase_uom = Column(String, nullable=True)
    purchase_uom_conversion_rate = Column(Float, nullable=True)
    batch_tracked = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    variants = relationship("ProductVariant", back_populates="product")

class ProductVariant(Base):
    __tablename__ = "product_variants"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    sales_price = Column(Float)
    purchase_price = Column(Float)
    type = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="variants")

class ConfigAttribute(Base):
    __tablename__ = "config_attributes"

    id = Column(Integer, primary_key=True, index=True)
    config_name = Column(String)
    config_value = Column(String)

    variant_id = Column(Integer, ForeignKey("product_variants.id"))
