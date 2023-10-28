from sqlalchemy import create_engine
from db.Classes import cWischlists,cBase,cwischs
from sqlalchemy.orm import Session
from sqlalchemy import select

engine = create_engine("sqlite:///db/test.db", echo=True)
cBase.metadata.create_all(engine)
session = Session(engine)

def wlist_to_id(wlist:str)->str:
    stmt = (
        select(
            cWischlists.id
        ).where(cWischlists.name == wlist.upper())
    )
    return session.scalars(stmt).__next__()

def get_wisches_data(wlist:str)->dict:
    stmt = (
        select(
            cWischlists
        ).where(cWischlists.name == wlist)
    )

    x = session.scalars(stmt).__next__()

    return {
        "name":x.name,
        "fullname":x.fullname,
        "allcost":x.allcost,
        "discrichon":x.discrichon
    }

def get_wisch(wid:int) -> dict:
    stmt = (
        select(
            cwischs
        ).where(cwischs.id == wid)
    )

    x = session.scalars(stmt).__next__()

    return {
        "name":x.name,
        "fullname":x.fullname,
        "link":x.link,
        "price":x.price,
        "discrichon":x.discrichon,
        "id":x.id
    }

def get_wisches(wlist:str)->list[int]:

    stmt = (
        select(
            cwischs.id
        ).where(cwischs.wlid == wlist_to_id(wlist))
    )

    return list(session.scalars(stmt))

def get_wisch_ids():
    stmt = (
        select(
            cwischs.id
        )
    )
    return list(session.scalars(stmt))

def get_wlists_nams()->list[str]:
    stmt = (
        select(
            cWischlists.name
        )
    )
    return list(session.scalars(stmt))