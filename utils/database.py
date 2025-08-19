import os
import uuid
import asyncio
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from sqlalchemy import text, and_
from sqlalchemy.orm import sessionmaker
from typing import Optional, List
from datetime import timedelta, timezone, datetime
from schemas.models import User, Class, Enrollment

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


async def get_user_by_id(id: uuid.UUID) -> Optional[User]:
    async with AsyncSessionLocal() as session:
        stmt = select(User).where(User.id==id)
        result = await session.scalars(stmt)
        user = result.one_or_none()
    
    return user


    
        

