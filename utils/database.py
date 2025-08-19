import os
import uuid
import asyncio
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from sqlalchemy import text, and_, delete
from sqlalchemy.orm import sessionmaker
from typing import Optional, List, Tuple
from datetime import timedelta, timezone, datetime
from db_schemas.models import User, Class, Enrollment

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=15,
    pool_timeout=30,
    pool_recycle=1800,
    echo=False
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False
)

# ------------------ User Table -------------------------
async def get_user_by_id(id: uuid.UUID) -> Tuple[Optional[User], str]:
    try:
        async with AsyncSessionLocal() as session:
            stmt = select(User).where(User.id==id)
            result = await session.scalars(stmt)
            user = result.one_or_none()
            
            if user:
                return user, "User found"
            
            return None, "User not found"
    except Exception as e:
        return None, f"Error fetching user: {e}"
    
    
async def get_user_by_id(id: uuid.UUID) -> Tuple[Optional[User], str]:
    try:
        async with AsyncSessionLocal() as session:
            stmt = select(User).where(User.id==id)
            result = await session.scalars(stmt)
            user = result.one_or_none()
            
            if user:
                return user, "User found"
            
            return None, "User not found"
    except Exception as e:
        return None, f"Error fetching user: {e}"
    
    
async def get_user_by_username_or_email(username_or_email: str) -> Tuple[Optional[User], str]:
    try:
        async with AsyncSessionLocal() as session:
            stmt = select(User).where(User.username==username_or_email | User.email==username_or_email)
            result = await session.scalars(stmt)
            user = result.one_or_none()
            
            if user:
                return user, "User found"
            
            return None, "User not found"
    except Exception as e:
        return None, f"Error fetching user: {e}"


async def insert_user(username: str, email: str, password: str) -> Tuple[bool, str]:
    try:
        async with AsyncSessionLocal() as session:
            stmt = select(User).where(User.name==username | User.email==email)
            result = await session.scalars(stmt)
            user = result.one_or_none()            
            
            if not user:
                return False, "Username or Email already exist!"
            
            new_user = User(username=username, email=email, password=password)
            session.add(new_user)
            await session.commit()
        return True, "User registered successfully"
    except Exception as e:
        return False, f"Unexpected error: {e}"
            
# ----------------- Class Table ---------------------------
async def get_all_classes() -> Tuple[List[Class], str]:
    try:
        async with AsyncSessionLocal() as session:
            stmt = select(Class)
            result = await session.scalars(stmt)
            classes = result.all()
            
            if not classes:
                return classes, "No classes found"
        return classes, "Classes retrieved successfully"
    except Exception as e:
        return [], f"Error fetching classes: {e}"
    
    
async def get_classes_by_id(id: uuid.UUID) -> Tuple[Optional[Class], str]:
    try:
        async with AsyncSessionLocal() as session:
            stmt = select(Class).where(Class.id==id)
            result = await session.scalars(stmt)
            classes = result.one_or_none()
            
            if not classes:
                return None, "No classes found"
        return classes, "Classes retrieved successfully"
    except Exception as e:
        return None, f"Error fetching classes: {e}"
    
    
async def insert_classes(name: str, detail: str = None) -> Tuple[bool, str]:
    try:
        async with AsyncSessionLocal() as session:
            stmt = select(Class).where(Class.name==name)
            result = await session.scalars(stmt)
            classes = result.one_or_none() 
            
            if not classes:
                return False, "Class name already exists!"
            
            new_class = Class(name=name, detail=detail)
            session.add(new_class)
            await session.commit()
        return True, "Class added successfully"
    except Exception as e:
        return False, f"Unexpected error: {e}"


async def update_classes_by_id(id: uuid.UUID, name: str = None, detail: str = None) -> Tuple[bool, str]:
    try:
        async with AsyncSessionLocal() as session:
            stmt = select(Class).where(Class.id==id)
            result = await session.scalars(stmt)
            classes = result.one_or_none()
        
            if classes:
                if name:
                    classes.name = name
                if detail:
                    classes.detail = detail
                    
                await session.commit()
            else:
                return False, "No classes found"
        return True, "Update success"
    except Exception as e:
        return False, f"Error update classes: {e}"
    
    
async def delete_classes_by_id(id: uuid.UUID) -> Tuple[bool, str]:
    try:
        async with AsyncSessionLocal() as session:
            stmt = delete(Class).where(Class.id==id)
            result = await session.execute(stmt)
            await session.commit()
            
            if result.rowcount == 0:
                return False, "No classes found"
        return True, "Delete success"
    except Exception as e:
        return False,"Error update classes: {e}"