from fastapi import APIRouter


router = APIRouter()


@router.get("")
async def create():
    return {"succes": 200, "message": "something was created"}
