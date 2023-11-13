import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source/server/resolvers")
sys.path.append("D:/Program/Programing/Projects/model_agency/source/server")

from models_db import administrators
from resolvers import administrators


administrators_router = fastapi.APIRouter(prefix='/administrators', tags=["Administrators"])


@administrators_router.get(path='/get/{administrator_id}', response_model=dict)
def get_administrator(administrator_id: int) -> dict:
    return administrators.get(administrator_id = administrator_id)

@administrators_router.get(path='/get', response_model=dict)
def get_administrators() -> dict:
    return administrators.get_all()

@administrators_router.post(path='/new', response_model=dict)
def new_administrator(administrator: administrators) -> dict:
    return administrators.new(administrator = administrator)

##@administrators_router.put(path='/updateNumberPhone/{administrator_id}', response_model=dict)
##def update_number_phone(administrator : administrators) -> dict:
    ##return administrators.get(administrator = administrator)

##@administrators_router.delete(path='/delete/{administrator_id}', response_model=dict)
##def delete_administrator(administrator_id: int) -> dict:
     ##return administrators.delete(administrator_id = administrator_id)
