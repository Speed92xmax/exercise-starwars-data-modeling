import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Product (Base):
    __tablename__="product"

    id= Column(Integer,primary_key=True)
    name= Column(String(100),nullable=False)
    details= Column(String(250),nullable=False)
    image_src= Column(String(250),nullable=False)
    price=Column(Integer,nullable=True)
    category_product =relationship("category_product")

class Category(Base):
    __tablename__="category"

    id= Column(Integer,primary_key=True)
    name= Column (String(100),nullable=False)
    description = Column(String(250),nullable=True)
    category_product =relationship("category_product")

class CategoryProduct (Base):
    __tablename__="category_product"

    id= Column( Integer,primary_key=True)
    product_id= Column(Integer, ForeignKey("product.id"),nullable=False)
    category_id= Column(Integer, ForeignKey("category.id"),nullable=False)

render_er(Base,'diagam.png')