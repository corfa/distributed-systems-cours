from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from db.requests.links import create_links, get_link_by_id, change_status
from broker.actions import put_in_queue
from pika.adapters.blocking_connection import BlockingChannel
from api.depends import get_db, get_broker, get_digit_header
from models.links import Item, Status

router = APIRouter()


@router.get("/links/{link_id}")
async def get_link(link_id: int, db: Session = Depends(get_db)):
    link = get_link_by_id(db, link_id)
    return JSONResponse(content=link, headers=get_digit_header())


@router.post("/links/", response_model=Item)
async def create_link(item: Item, db: Session = Depends(get_db),  broker: BlockingChannel = Depends(get_broker) ):
    id_links =  create_links(db, item.url)
    put_in_queue(broker, item.url,id_links)
    return JSONResponse(content= {"id": id_links, 'url':item.url}, headers=get_digit_header())



@router.put("/links/{link_id}", response_model=Status)
async def put_link(link_id: int,status: Status, db: Session = Depends(get_db)):
    change_status(db, link_id, status.status)
    return JSONResponse(content= {"id":link_id,"status": status.status}, headers=get_digit_header())



