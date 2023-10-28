
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import column_property
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy import select
from typing import Optional
from typing import List


class cBase(DeclarativeBase):pass

class cwischs(cBase):
    __tablename__ = "wischs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    link: Mapped[Optional[str]]
    price: Mapped[float]
    discrichon: Mapped[Optional[str]]
    wlid: Mapped[int] = mapped_column(ForeignKey("wischlists.id"))
    wl: Mapped["cWischlists"] = relationship(back_populates="wlist")

class cWischlists(cBase):
    __tablename__ = "wischlists"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    discrichon: Mapped[Optional[str]]
    allcost: Mapped[float] = column_property(
        select(
            func.sum(cwischs.price)
        )
        .where(cwischs.wlid == id)
        .correlate_except()
        .scalar_subquery()
    )
    wlist: Mapped[List["cwischs"]] = relationship(
        back_populates="wl", cascade="all, delete-orphan"
    )

