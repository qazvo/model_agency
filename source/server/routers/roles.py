import fastapi

from models_db import roles
from resolvers import roles_res


roles_router = fastapi.APIRouter(prefix='/roles', tags=["Roles"])


@roles_router.get(path='/get/{role_id}', response_model=dict)
def get_role(role_id: int) -> dict:
    return roles_res.get(role_id = role_id)

@roles_router.get(path='/get', response_model=dict)
def get_roles() -> dict:
    return roles_res.get_all()

@roles_router.post(path='/new', response_model=dict)
def new_role(role: roles) -> dict:
    return roles_res.new(role = role)

@roles_router.put(path='/updatePermission/{role_id}', response_model=dict)
def update_permission(role: roles) -> dict:
    return roles_res.update(role = role)

@roles_router.delete(path='/delete/{role_id}', response_model=dict)
def delete_role(role_id: int) -> dict:
     return roles_res.delete(role_id = role_id)