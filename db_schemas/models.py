from sqlalchemy import Column, text, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()")
    )
    username = Column(String(50), nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    level = Column(String(10), nullable=False, server_default="user")
    
    
class Class(Base):
    __tablename__ = "classes"
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()")
    )
    name = Column(String(256), nullable=False, unique=True)
    detail = Column(String, nullable=True)
    
    
class Enrollment(Base):
    __tablename__ = "enrollments"
    
    user_id = mapped_column(ForeignKey("users.id"), primary_key=True)
    class_id = mapped_column(ForeignKey("classes.id"), primary_key=True)
    enrolled_at = Column(DateTime(timezone=True))