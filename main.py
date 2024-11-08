import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger

# Настройка логирования с использованием loguru для вывода в консоль
logger.add(sys.stderr, level="INFO")

DATABASE_URL = "postgresql://user:password@db:5432/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

app = FastAPI()

# Функция для очистки базы данных
def clear_database():
    logger.info("Clearing database")
    db = SessionLocal()
    try:
        db.execute(text("TRUNCATE TABLE items RESTART IDENTITY CASCADE;"))
        db.commit()
    except Exception as e:
        logger.error("Error clearing database: {}", e)
        db.rollback()
    finally:
        db.close()

# Применяем очистку базы данных при запуске приложения
clear_database()

Base.metadata.create_all(bind=engine)

class ItemCreate(BaseModel):
    name: str
    description: str

@app.post("/items/", response_model=ItemCreate)
def create_item(item: ItemCreate):
    logger.info("Creating item: {}", item.name)
    db = SessionLocal()
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    logger.info("Item created: {}", db_item.id)
    return db_item

@app.get("/items/{item_id}", response_model=ItemCreate)
def read_item(item_id: int):
    logger.info("Reading item: {}", item_id)
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        logger.warning("Item not found: {}", item_id)
        raise HTTPException(status_code=404, detail="Item not found")
    logger.info("Item read: {}", db_item.id)
    return db_item

@app.put("/items/{item_id}", response_model=ItemCreate)
def update_item(item_id: int, item: ItemCreate):
    logger.info("Updating item: {}", item_id)
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        logger.warning("Item not found: {}", item_id)
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    logger.info("Item updated: {}", db_item.id)
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    logger.info("Deleting item: {}", item_id)
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        logger.warning("Item not found: {}", item_id)
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    logger.info("Item deleted: {}", item_id)
    return {"detail": "Item deleted"}
