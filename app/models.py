from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"  # PostgreSQL のテーブル名と一致すること

    customer_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    store_id = Column(Integer, nullable=False)
    address_id = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False)
    create_date = Column( DateTime,nullable=False)
    last_update = Column( DateTime,nullable=False)

class Payment(Base):
    __tablename__ = "payment"  # PostgreSQL のテーブル名と一致すること

    payment_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False)
    staff_id = Column(Integer, nullable=False)
    rental_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    payment_date = Column(DateTime, nullable=False)



