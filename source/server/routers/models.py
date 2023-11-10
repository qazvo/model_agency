import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from source.server.models_db import models
from source.server.resolvers import models


models_router = fastapi.APIRouter(prefix='/models', tags=["Models"])


@models_router.get(path='/get/{model_id}', response_model=dict)
def get_model(model_id: int) -> dict:
    return models.get(model_id = model_id)

@models_router.get_all(path='/get', response_model=dict)
def get_models() -> dict:
    return models.get_all()

@models_router.new(path='/new/{model_id}', response_model=dict)
def new_model(model: models) -> dict:
    return models.new(model = model)

@models_router.put(path='/updateNumberPhone/{model_id}', response_model=dict)
def update_number_phone(model_id: int, new_number_phone: models.number_phone) -> dict:
    return models.get(model_id = model_id, new_number_phone = new_number_phone)

@models_router.delete(path='/delete/{model_id}', response_model=dict)
def delete_model(model_id: int) -> dict:
     return models.delete(model_id = model_id)