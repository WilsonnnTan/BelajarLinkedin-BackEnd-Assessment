from fastapi import APIRouter, HTTPException, status, Depends
from api_schemas.auth import UserRegister, Token
from passlib.context import CryptContext
from datetime import timedelta
from utils.database import insert_user, get_user_by_username_or_email
from utils.auth import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# register
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister):
    hashed_pw = pwd_context.hash(user.password)
    is_success, msg = await insert_user(user.username, user.email, hashed_pw)
    if not is_success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    return { "msg": "User registered successfully" }
            

# login
@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login(user: OAuth2PasswordRequestForm = Depends()):
    dbuser, msg = await get_user_by_username_or_email(user.username)
    if not dbuser or not pwd_context.verify(user.password, dbuser.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Username or Password")
    
    access_token = create_access_token(
        data={"sub": dbuser.id, "username": dbuser.username},
        expires_delta=timedelta(minutes=30)
    )
    return { "access_token": access_token, "token_type": "bearer" }