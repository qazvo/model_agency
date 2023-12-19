import fastapi

from models_db import customer_organizations
from resolvers import customer_organizations_res


customer_organizations_router = fastapi.APIRouter(prefix='/customer_organizations', tags=["Customer_organizations"])


@customer_organizations_router.get(path='/get/{customer_organization_id}', response_model=dict)
def get_customer_organization(customer_organization_id: int) -> dict:
    return customer_organizations_res.get(customer_organization_id = customer_organization_id)

@customer_organizations_router.get(path='/get', response_model=dict)
def get_customer_organizations() -> dict:
    return customer_organizations_res.get_all()

@customer_organizations_router.post(path='/new', response_model=dict)
def new_customer_organization(customer_organization: customer_organizations) -> dict:
    return customer_organizations_res.new(customer_organization = customer_organization)

@customer_organizations_router.put(path='/updateContactDetails/{customer_organization_id}', response_model=dict)
def update_contact_details(customer_organization: customer_organizations) -> dict:
    return customer_organizations_res.update(customer_organization = customer_organization)

@customer_organizations_router.delete(path='/delete/{customer_organization_id}', response_model=dict)
def delete_customer_organization(customer_organization_id: int) -> dict:
     return customer_organizations_res.delete(customer_organization_id = customer_organization_id)