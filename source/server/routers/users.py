import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from source.server.models_db import users
from source.server.resolvers import users


users_router = fastapi.APIRouter(prefix='/users', tags=["Users"])


@users_router.get(path='/get/{user_id}', response_model=dict)
def get_user(user_id: int) -> dict:
    return users.get(user_id = user_id)

@users_router.get_all(path='/get', response_model=dict)
def get_users() -> dict:
    return users.get_all()

@users_router.new(path='/new/{user_id}', response_model=dict)
def new_user(user: users) -> dict:
    return users.new(user = user)

@users_router.put(path='/updatePassword/{user_id}', response_model=dict)
def update_password(user_id: int, new_password: users.password) -> dict:
    return users.get(user_id = user_id, new_password = new_password)

@users_router.delete(path='/delete/{user_id}', response_model=dict)
def delete_user(user_id: int) -> dict:
     return users.delete(user_id = user_id)