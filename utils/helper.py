from fastapi import HTTPException, status

def error_exception(message: str):
    if message.startswith("Error"):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message)