import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from source.server.models_db import contracts
from source.server.resolvers import contracts


contracts_router = fastapi.APIRouter(prefix='/contracts', tags=["Contracts"])


@contracts_router.get(path='/get/{contract_id}', response_model=dict)
def get_contract(contract_id: int) -> dict:
    return contracts.get(contract_id = contract_id)

@contracts_router.get_all(path='/get', response_model=dict)
def get_contracts() -> dict:
    return contracts.get_all()

@contracts_router.new(path='/new/{contract_id}', response_model=dict)
def new_contract(contract: contracts) -> dict:
    return contracts.new(contract = contract)

@contracts_router.put(path='/updatePayment/{contract_id}', response_model=dict)
def update_payment(contract_id: int, new_payment: contracts.payment) -> dict:
    return contracts.get(contract_id = contract_id, new_payment = new_payment)

@contracts_router.delete(path='/delete/{contract_id}', response_model=dict)
def delete_contract(contract_id: int) -> dict:
     return contracts.delete(contract_id = contract_id)
