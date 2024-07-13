from sqlalchemy import Column, Integer, String, Enum, Text, DECIMAL, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..database import Base
from enum import Enum as PyEnum


class UserRole(PyEnum):
    admin = "admin"
    user = "user"


class User(Base):
    __tablename__ = 'users'  # Corrected __tablename__

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password_hash = Column(String(255), nullable=False)
    phone = Column(String(50))
    address = Column(Text)
    role = Column(Enum(UserRole), default=UserRole.user)

    orders = relationship('Order', back_populates='user')


class Category(Base):
    __tablename__ = 'categories'  # Corrected __tablename__

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)

    products = relationship('Product', back_populates='category')


class Product(Base):
    __tablename__ = 'products'  # Corrected __tablename__

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))

    category = relationship('Category', back_populates='products')
    order_details = relationship('OrderDetail', back_populates='product')
    inventory_entries = relationship('Inventory', back_populates='product')


class Order(Base):
    __tablename__ = 'orders'  # Corrected __tablename__

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    order_date = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)

    user = relationship('User', back_populates='orders')
    order_details = relationship('OrderDetail', back_populates='order')


class OrderDetail(Base):
    __tablename__ = 'order_details'  # Corrected __tablename__

    order_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship('Order', back_populates='order_details')
    product = relationship('Product', back_populates='order_details')


class Supplier(Base):
    __tablename__ = 'suppliers'  # Corrected __tablename__

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    contact_person = Column(String(255), nullable=False)
    phone = Column(String(50))
    email = Column(String(255))
    address = Column(Text)

    inventory_entries = relationship('Inventory', back_populates='supplier')


class Inventory(Base):
    __tablename__ = 'inventory'  # Corrected __tablename__

    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'))
    quantity = Column(Integer, nullable=False)
    received_date = Column(DateTime, nullable=False)

    product = relationship('Product', back_populates='inventory_entries')
    supplier = relationship('Supplier', back_populates='inventory_entries')
