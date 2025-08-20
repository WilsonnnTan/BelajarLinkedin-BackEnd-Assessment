import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from utils.auth import get_current_user
from utils.database import get_enrollment_by_user_id, enroll_user
from utils.helper import error_exception

router = APIRouter()

# Kelas yang sudah diambil User
@router.get("/", status_code=status.HTTP_200_OK)
async def enrollment_list(current_user=Depends(get_current_user)):
    enrollment, msg = await get_enrollment_by_user_id(current_user.id)
    error_exception(msg)
    
    return { "data": enrollment, "message": msg }

# User enroll kelas
@router.post("/{class_id}", status_code=status.HTTP_201_CREATED)
async def enroll(class_id: uuid.UUID, current_user=Depends(get_current_user)):
    is_success, msg = await enroll_user(current_user.id, class_id)
    if not is_success:
        error_exception(msg)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    
    return { "message": msg }