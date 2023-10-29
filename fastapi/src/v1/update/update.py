from fastapi import APIRouter


router = APIRouter()


@router.get("")
async def update():
    return {"succes": 200, "message": "something was updated"}
