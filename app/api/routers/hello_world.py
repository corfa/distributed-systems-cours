from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.depends import get_digit_header

router = APIRouter()


@router.get("/hello/", tags=["hello"])
async def hello():
    
    return JSONResponse(content={'hello':'world'}, headers=get_digit_header())