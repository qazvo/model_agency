import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from source.server.models_db import customer_organizations
from source.server.resolvers import customer_organizations


customer_organizations_router = fastapi.APIRouter(prefix='/customer_organizations', tags=["Customer_organizations"])


@customer_organizations_router.get(path='/get/{customer_organization_id}', response_model=dict)
def get_customer_organization(customer_organization_id: int) -> dict:
    return customer_organizations.get(customer_organization_id = customer_organization_id)

@customer_organizations_router.get_all(path='/get', response_model=dict)
def get_customer_organizations() -> dict:
    return customer_organizations.get_all()

@customer_organizations_router.new(path='/new/{customer_organization_id}', response_model=dict)
def new_customer_organization(customer_organization: customer_organizations) -> dict:
    return customer_organizations.new(customer_organization = customer_organization)

@customer_organizations_router.put(path='/updateContactDetails/{customer_organization_id}', response_model=dict)
def update_contact_details(customer_organization_id: int, new_contact_details: customer_organizations.contact_details) -> dict:
    return customer_organizations.get(customer_organization_id = customer_organization_id, new_contact_details = new_contact_details)

@customer_organizations_router.delete(path='/delete/{customer_organization_id}', response_model=dict)
def delete_customer_organization(customer_organization_id: int) -> dict:
     return customer_organizations.delete(customer_organization_id = customer_organization_id)