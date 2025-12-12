from fastapi import APIRouter

# Initilize router
router = APIRouter()

# /ping
@router.get("/ping")
def ping():
    return {"status": "ok"}