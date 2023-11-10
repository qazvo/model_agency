import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from source.server.models_db import countries
from source.server.resolvers import countries


countries_router = fastapi.APIRouter(prefix='/countries', tags=["Countries"])


@countries_router.get(path='/get/{country_id}', response_model=dict)
def get_country(country_id: int) -> dict:
    return countries.get(country_id = country_id)

@countries_router.get_all(path='/get', response_model=dict)
def get_countries() -> dict:
    return countries.get_all()

@countries_router.new(path='/new/{country_id}', response_model=dict)
def new_country(country: countries) -> dict:
    return countries.new(country = country)

@countries_router.put(path='/updateName/{country_id}', response_model=dict)
def update_name(country_id: int, new_name: countries.name) -> dict:
    return countries.get(country_id = country_id, new_name = new_name)

@countries_router.delete(path='/delete/{country_id}', response_model=dict)
def delete_country(country_id: int) -> dict:
     return countries.delete(country_id = country_id)