from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from app.databases.db import Base


class ConsultingRoom(Base):
    __tablename__ = "consulting_rooms"

    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String(20), nullable=False)
    location = Column(String(250), nullable=False)

    doctor_rooms = relationship("DoctorRoom", back_populates="consulting_room")
