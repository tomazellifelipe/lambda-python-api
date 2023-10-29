from fastapi import APIRouter
from http import HTTPStatus

from src.utils.http_response import build_response

router = APIRouter()


@router.get("")
async def create():
    return build_response(HTTPStatus.OK, body={"message": "something was created"})
