from sqlalchemy import Column, text, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column, relationship

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
    
    # cascade delete: deleting a user automatically deletes enrollments
    enrollments = relationship(
        "Enrollment",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    
class Class(Base):
    __tablename__ = "classes"
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()")
    )
    name = Column(String(256), nullable=False, unique=True)
    detail = Column(String, nullable=True)
    
    # cascade delete: deleting a class automatically deletes its enrollments
    enrollments = relationship(
        "Enrollment", 
        back_populates="class_", 
        cascade="all, delete-orphan", 
        passive_deletes=True
    )
    
    
class Enrollment(Base):
    __tablename__ = "enrollments"
    
    user_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    class_id = mapped_column(ForeignKey("classes.id", ondelete="CASCADE"), primary_key=True)
    enrolled_at = Column(DateTime(timezone=True))
    
    user = relationship("User", back_populates="enrollments")
    class_ = relationship("Class", back_populates="enrollments")