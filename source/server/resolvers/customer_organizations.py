from server.database.db_manager import db_manager

from server.models_db import customer_organizations

def get(customer_organization_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * FROM customer_organizations WHERE id = ?""", 
                              args=(customer_organization_id,))
    return res
    
def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * FROM customer_organizations""",
                             many=True)
    return res

def new(customer_organization: customer_organizations) -> dict:
    res = db_manager.execute(query="""INSERT INTO customer_organizations(id, name, country_id, contact_details, inn, confirmed) 
                                       VALUES(?, ?, ?, ?, ?, ?) 
                                       RETURNING id""", 
                              args=(customer_organization.id, customer_organization.name, customer_organization.country_id, customer_organization.contact_details, customer_organization.inn, customer_organization.confirmed))
    return res

def update(customer_organization_id: int, new_contact_details: customer_organizations.contact_details) -> dict:
    res = db_manager.execute(query="""UPDATE customer_organizations 
                                        SET contact_details = ?
                                        WHERE id = ?""", 
                              args=(new_contact_details, customer_organization_id))
    return res

def delete(customer_organization_id: int) -> dict:
    res = db_manager.execute(query="""DELETE * FROM customer_organizations WHERE id = ?""", 
                              args=(customer_organization_id,))
    return res