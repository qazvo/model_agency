import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from models_db import users
from resolvers import users_res


users_router = fastapi.APIRouter(prefix='/users', tags=["Users"])


@users_router.get(path='/get/{user_id}', response_model=dict)
def get_user(user_id: int) -> dict:
    return users_res.get(user_id = user_id)

@users_router.get(path='/get', response_model=dict)
def get_users() -> dict:
    return users_res.get_all()

@users_router.post(path='/new', response_model=dict)
def new_user(user: users) -> dict:
    return users_res.new(user = user)

@users_router.put(path='/updatePassword/{user_id}', response_model=dict)
def update_password(user: users) -> dict:
    return users_res.update(user = user)

@users_router.delete(path='/delete/{user_id}', response_model=dict)
def delete_user(user_id: int) -> dict:
     return users_res.delete(user_id = user_id)