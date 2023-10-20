from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.requests.links import create_links, get_link_by_id

from api.depends import get_db
from models.links import Item

router = APIRouter()


@router.get("/links/{link_id}")
async def get_link(link_id: int, db: Session = Depends(get_db)):
    link = get_link_by_id(db, link_id)
    return link


@router.post("/links/", response_model=Item)
async def create_link(item: Item, db: Session = Depends(get_db)):
    id_links =  create_links(db, item.url)
    return {"id": id_links, 'url':item.url}


