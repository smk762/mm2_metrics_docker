from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import session
from model import SwapsTable, FailedTable, Swap, FailedSwap

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_swaps():
    resp = {"msg":"Welcome to Atomicdex swaps API. Check /docs for available endpoints."}
    return resp

@app.get("/swaps")
def read_swaps():
    swaps = session.query(SwapsTable).all()
    return swaps

@app.get("/swaps/{uuid}")
def read_swap(uuid: int):
    swap = session.query(SwapsTable).\
        filter(SwapsTable.uuid == uuid).first()
    return swap
'''
@app.post("/user")
async def create_user(name: str, age: int):
    user = UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()

@app.put("/users")
async def update_users(users: List[User]):
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        session.commit()
'''