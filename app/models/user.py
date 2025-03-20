from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from app.databases.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String(200), nullable=False)
    last_login = Column(DateTime, nullable=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    dni = Column(String(20), unique=True, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    email = Column(String(80), unique=True, nullable=False)
    username = Column(String(45), unique=True, nullable=False)
    role = Column(String(20), nullable=False, default="patient")
    phone = Column(String(20), nullable=True)
    date_joined = Column(DateTime, server_default=func.now())
    city = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    address = Column(String(200), nullable=True)

    doctor = relationship("Doctor", back_populates="user", uselist=False)
    patient = relationship("Patient", back_populates="user", uselist=False)
