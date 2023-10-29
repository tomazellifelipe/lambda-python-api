from fastapi import APIRouter

from src.v1.create import create
from src.v1.read import read
from src.v1.update import update
from src.v1.delete import delete


router = APIRouter()
router.include_router(create.router, prefix="/create", tags=["Create"])
router.include_router(read.router, prefix="/read", tags=["Read"])
router.include_router(update.router, prefix="/update", tags=["Update"])
router.include_router(delete.router, prefix="/delete", tags=["Delete"])
