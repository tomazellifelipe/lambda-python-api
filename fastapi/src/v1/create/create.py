from fastapi import APIRouter
from http import HTTPStatus

from src.utils.http_response import build_response
from src.v1.schemas.item import Item

router = APIRouter()


@router.post("")
async def create(item: Item):
    message = f"item {item.name} was created with price R${item.price:.2f}"
    return build_response(HTTPStatus.OK, body={"message": message})
