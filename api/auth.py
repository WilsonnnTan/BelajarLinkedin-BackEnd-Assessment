from fastapi import APIRouter, HTTPException, status
from api_schemas.auth import UserLogin, UserRegister, Token
from passlib.context import CryptContext
from datetime import timedelta
from utils.database import insert_user, get_user_by_username_or_email
from utils.auth import create_access_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# register
@router.post("/register")
async def register(user: UserRegister):
    hashed_pw = pwd_context.hash(user.password)
    is_success, msg = await insert_user(user.username, user.email, hashed_pw)
    if not is_success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    return { "msg": "User registered successfully" }
            

# login
@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    dbuser, msg = await get_user_by_username_or_email(user.username_or_email)
    if not dbuser or not pwd_context.verify(user.password, dbuser.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or Password is wrong")
    
    access_token = create_access_token(
        data={"sub": dbuser.id, "username": dbuser.username},
        expires_delta=timedelta(minutes=30)
    )
    return { "access_token": access_token, "token_type": "bearer" }