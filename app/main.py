from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/v1/products/create")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    try:
        # Create Product object
        db_product = models.Product(**product.dict(exclude={"variants"}))
        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        # Create ProductVariant objects
        for variant in product.variants:
            db_variant = models.ProductVariant(**variant.dict(), product_id=db_product.id)
            db.add(db_variant)

            # Create ConfigAttribute objects
            for config_attribute in variant.config_attributes:
                db_config_attribute = models.ConfigAttribute(**config_attribute.dict(), variant_id=db_variant.id)
                db.add(db_config_attribute)

        db.commit()
        db.refresh(db_product)
        return db_product

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
