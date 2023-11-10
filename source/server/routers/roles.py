import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from source.server.models_db import roles
from source.server.resolvers import roles


roles_router = fastapi.APIRouter(prefix='/roles', tags=["Roles"])


@roles_router.get(path='/get/{role_id}', response_model=dict)
def get_role(role_id: int) -> dict:
    return roles.get(role_id = role_id)

@roles_router.get_all(path='/get', response_model=dict)
def get_roles() -> dict:
    return roles.get_all()

@roles_router.new(path='/new/{role_id}', response_model=dict)
def new_role(role: roles) -> dict:
    return roles.new(role = role)

@roles_router.put(path='/updatePermission/{role_id}', response_model=dict)
def update_permission(role_id: int, new_permission: roles.permission) -> dict:
    return roles.get(role_id = role_id, new_permission = new_permission)

@roles_router.delete(path='/delete/{role_id}', response_model=dict)
def delete_role(role_id: int) -> dict:
     return roles.delete(role_id = role_id)