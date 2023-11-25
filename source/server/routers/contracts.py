import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from models_db import contracts
from resolvers import contracts_res


contracts_router = fastapi.APIRouter(prefix='/contracts', tags=["Contracts"])


@contracts_router.get(path='/get/{contract_id}', response_model=dict)
def get_contract(contract_id: int) -> dict:
    return contracts_res.get(contract_id = contract_id)

@contracts_router.get(path='/get', response_model=dict)
def get_contracts() -> dict:
    return contracts_res.get_all()

@contracts_router.post(path='/new', response_model=dict)
def new_contract(contract: contracts) -> dict:
    return contracts_res.new(contract = contract)

@contracts_router.put(path='/updatePayment/{contract_id}', response_model=dict)
def update_payment(contract: contracts) -> dict:
    return contracts_res.update(contract = contract)

@contracts_router.delete(path='/delete/{contract_id}', response_model=dict)
def delete_contract(contract_id: int) -> dict:
     return contracts_res.delete(contract_id = contract_id)
