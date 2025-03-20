from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
from app.databases.db import Base


class DoctorRoom(Base):
    __tablename__ = "doctor_rooms"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("consulting_rooms.id"), nullable=False)
    assigned_date = Column(DateTime, server_default=func.now())

    doctor = relationship("Doctor", back_populates="doctor_rooms")
    consulting_room = relationship("ConsultingRoom", back_populates="doctor_rooms")
