from fastapi import APIRouter


router = APIRouter()


@router.get("")
async def read():
    return {"succes": 200, "message": "something was read"}
