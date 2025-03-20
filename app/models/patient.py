from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.databases.db import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)

    user = relationship("User", back_populates="patient", uselist=False)
    appointments = relationship("Appointment", back_populates="patient")
