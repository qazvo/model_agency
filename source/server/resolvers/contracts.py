from server.database.db_manager import db_manager

from server.models_db import contracts

def get(contract_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * FROM contracts WHERE id = ?""", 
                              args=(contract_id,))
    return res
    
def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * FROM contracts""",
                             many=True)
    return res

def new(contract: contracts) -> dict:
    res = db_manager.execute(query="""INSERT INTO contracts(id, event_id, model_id, payment) 
                                       VALUES(?, ?, ?, ?) 
                                       RETURNING id""", 
                              args=(contract.id, contract.event_id, contract.model_id, contract.payment))
    return res

def update(contract_id: int, new_payment: contracts.payment) -> dict:
    res = db_manager.execute(query="""UPDATE contracts 
                                        SET payment = ?
                                        WHERE id = ?""", 
                              args=(new_payment, contract_id))
    return res

def delete(contract_id: int) -> dict:
    res = db_manager.execute(query="""DELETE * FROM contracts WHERE id = ?""", 
                              args=(contract_id,))
    return res