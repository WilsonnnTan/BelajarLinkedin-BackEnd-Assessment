import os
import asyncio
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, APIRouter, status
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from api import auth, classes, enrollment

app = FastAPI()
router = APIRouter()
security = HTTPBearer()


@router.get("/")
async def root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)

app.include_router(router, tags=["Redirect to docs"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(classes.router, prefix="/class", tags=["class"])
app.include_router(enrollment.router, prefix="/enroll", tags=["enrollment"])