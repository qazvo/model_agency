import fastapi

from models_db import administrators
from resolvers import administrators_res


administrators_router = fastapi.APIRouter(prefix='/administrators', tags=["Administrators"])


@administrators_router.get(path='/get/{administrator_id}', response_model=dict)
def get_administrator(administrator_id: int) -> dict:
    return administrators_res.get(administrator_id = administrator_id)

@administrators_router.get(path='/get', response_model=dict)
def get_administrators() -> dict:
    return administrators_res.get_all()

@administrators_router.post(path='/new', response_model=dict)
def new_administrator(administrator: administrators) -> dict:
    return administrators_res.new(administrator = administrator)

@administrators_router.put(path='/updateNumberPhone/{administrator_id}', response_model=dict)
def update_number_phone(administrator: administrators) -> dict:
    return administrators_res.update(administrator = administrator)

@administrators_router.delete(path='/delete/{administrator_id}', response_model=dict)
def delete_administrator(administrator_id: int) -> dict:
     return administrators_res.delete(administrator_id = administrator_id)
