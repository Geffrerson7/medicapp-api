from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from app.databases.db import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    specialty = Column(String(100), nullable=False)
    identification_code = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)

    user = relationship("User", back_populates="doctor", uselist=False)
    appointments = relationship("Appointment", back_populates="doctor")
    schedules = relationship("Schedule", back_populates="doctor")
    doctor_rooms = relationship("DoctorRoom", back_populates="doctor")
