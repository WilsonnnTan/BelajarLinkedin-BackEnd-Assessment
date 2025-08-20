import uuid
from fastapi import Depends, APIRouter, HTTPException, status
from utils.auth import get_current_user
from utils.database import get_all_classes, get_classes_by_id, insert_classes, update_classes_by_id, delete_classes_by_id
from utils.helper import error_exception
from api_schemas.classes import AddClass, EditClass

router = APIRouter()


# lihat daftar kelas yang tersedia
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_class(current_user=Depends(get_current_user)):
    classes, msg = await get_all_classes()
    error_exception(msg)
    
    return { "data": classes, "message": msg }


# cek detail kelas
@router.get("/{class_id}", status_code=status.HTTP_200_OK)
async def get_class_by_id(class_id: uuid.UUID, current_user=Depends(get_current_user)):
    classes, msg = await get_classes_by_id(class_id)
    error_exception(msg)
    
    return { "data": classes, "message": msg }


# tambah kelas - admin privilege only (akun admin tersedia dari seeding database)
@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_class(classes: AddClass ,current_user=Depends(get_current_user)):
    if current_user.level != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    is_success, msg = await insert_classes(classes.name, classes.detail)
    if not is_success:
        error_exception(msg)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    
    return { "message": msg }


# edit kelas - admin privilege only 
@router.put("/{class_id}", status_code=status.HTTP_204_NO_CONTENT)
async def edit_class(class_id: uuid.UUID, classes: EditClass, current_user=Depends(get_current_user)):
    if current_user.level != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    is_success, msg = await update_classes_by_id(id=class_id, name=classes.name, detail=classes.detail)
    if not is_success:
        error_exception(msg)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg)


# hapus class - admin privilege only
@router.delete("/{class_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_class(class_id: uuid.UUID, current_user=Depends(get_current_user)):
    if current_user.level != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")

    is_success, msg = await delete_classes_by_id(class_id)
    if not is_success:
        error_exception(msg)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg)