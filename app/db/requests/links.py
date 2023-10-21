from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def create_links(db: Session, url: str) -> int:
    sql_query = "INSERT INTO links (url) VALUES (:url) RETURNING id"
    params = {"url": url}
    result = db.execute(text(sql_query), params)
    created_id = result.scalar()
    db.commit()
    return created_id


def get_link_by_id(db: Session, link_id: int):
    sql_query = "SELECT * FROM links WHERE id = :link_id"
    params = {"link_id": link_id}
    result = db.execute(text(sql_query), params)
    link = result.fetchone()
    if link:
        res = {'id':link[0],'url':link[1]}
        try:
            res['status'] = link[2]
        except:
            res['status'] = None
        finally:
            return res

    return link

def change_status(db: Session, link_id:int, link_status: int):
    sql_query = "UPDATE links set status = :link_status WHERE id = :link_id"
    params = {"link_id": link_id,'link_status':link_status}
    db.execute(text(sql_query), params)
    db.commit()
    return 1