from sqlalchemy import Column, Integer, String, DateTime, Float
from pydantic import BaseModel
from db import Base
from db import ENGINE
from datetime import date, datetime, time, timedelta

class SwapsTable(Base):
    __tablename__ = 'swaps'

    uuid = Column(String(36), primary_key=True)
    started_at = Column(DateTime)
    taker_coin = Column(String(8))
    taker_amount = Column(Float('20,8'))
    taker_gui = Column(String(32))
    taker_version = Column(String(128))
    taker_pubkey = Column(String(64))
    maker_coin = Column(String(8))
    maker_amount = Column(Float('20,8'))
    maker_gui = Column(String(32))
    maker_version = Column(String(128))
    maker_pubkey = Column(String(64))


class FailedTable(Base):
    __tablename__ = 'swaps_failed'

    uuid = Column(String(36), primary_key=True)
    started_at = Column(DateTime)
    taker_coin = Column(String(8))
    taker_amount = Column(Float('20,8'))
    taker_gui = Column(String(32))
    taker_version = Column(String(128))
    taker_pubkey = Column(String(64))
    maker_coin = Column(String(8))
    maker_amount = Column(Float('20,8'))
    maker_gui = Column(String(32))
    maker_version = Column(String(128))
    maker_pubkey = Column(String(64))
    taker_error_type = Column(String(32))
    taker_error_msg = Column(String(2048))
    taker_gui = Column(String(32))
    taker_version = Column(String(128))
    maker_error_type = Column(String(32))
    maker_error_msg = Column(String(2048))
    maker_gui = Column(String(32))
    maker_version = Column(String(128))


class Swap(BaseModel):
    uuid: str
    started_at: datetime
    taker_coin: str
    taker_amount: float
    taker_gui: str
    taker_version: str
    taker_pubkey: str
    maker_coin: str
    maker_amount: float
    maker_gui: str
    maker_version: str
    maker_pubkey: str


class FailedSwap(BaseModel):
    uuid: str
    started_at: datetime
    taker_coin: str
    taker_amount: float
    taker_gui: str
    taker_version: str
    taker_pubkey: str
    taker_error_type: str
    taker_error_msg: str
    maker_coin: str
    maker_amount: float
    maker_gui: str
    maker_version: str
    maker_pubkey: str    
    maker_error_type: str
    maker_error_msg: str


def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
