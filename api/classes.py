import uuid
from fastapi import Depends, APIRouter, HTTPException, status
from utils.auth import get_current_user
from utils.database import get_all_classes, get_classes_by_id, insert_classes, update_classes_by_id, delete_classes_by_id
from api_schemas.classes import AddClass, EditClass

router = APIRouter()

# liat daftar class yang tersedia
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_class(current_user=Depends(get_current_user)):
    classes, msg = await get_all_classes()
    if not classes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg)
    return { "data": classes, "message": msg }


# cek detail class
@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_class_by_id(id: uuid.UUID, current_user=Depends(get_current_user)):
    classes, msg = await get_classes_by_id(id)
    if not classes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg)
    return { "data": classes, "message": msg }


# tambah class
@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_class(classes: AddClass ,current_user=Depends(get_current_user)):
    if current_user.level != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    is_success, msg = insert_classes(AddClass.name, AddClass.detail)
    if not is_success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    
    return {}


# edit class - admin privilege only (akun admin tersedia dari seeding database)
@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def edit_class(id: uuid.UUID, classes: EditClass, current_user=Depends(get_current_user)):
    if current_user.level != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    is_success, msg = await update_classes_by_id(id=id, name=EditClass.name, detail=EditClass.detail)
    if not is_success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)


# hapus class - admin privilege only
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_class(id: uuid.UUID, current_user=Depends(get_current_user)):
    if current_user.level != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")

    is_success, msg = await delete_classes_by_id(id)
    if not is_success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)