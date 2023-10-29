from fastapi import APIRouter


router = APIRouter()


@router.get("")
async def delete():
    return {"succes": 200, "message": "something was deleted"}
