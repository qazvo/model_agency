import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from source.server.models_db import administrators
from source.server.resolvers import administrators


administrators_router = fastapi.APIRouter(prefix='/administrators', tags=["Administrators"])


@administrators_router.get(path='/get/{administrator_id}', response_model=dict)
def get_administrator(administrator_id: int) -> dict:
    return administrators.get(administrator_id = administrator_id)

@administrators_router.get_all(path='/get', response_model=dict)
def get_administrators() -> dict:
    return administrators.get_all()

@administrators_router.new(path='/new/{administrator_id}', response_model=dict)
def new_administrator(administrator: administrators) -> dict:
    return administrators.new(administrator = administrator)

@administrators_router.put(path='/updateNumberPhone/{administrator_id}', response_model=dict)
def update_number_phone(administrator_id: int, new_number_phone: administrators.number_phone) -> dict:
    return administrators.get(administrator_id = administrator_id, new_number_phone = new_number_phone)

@administrators_router.delete(path='/delete/{administrator_id}', response_model=dict)
def delete_administrator(administrator_id: int) -> dict:
     return administrators.delete(administrator_id = administrator_id)
