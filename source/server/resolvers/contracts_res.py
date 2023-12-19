from database.db_manager import db_manager

from models_db import contracts

def get(contract_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * FROM contracts WHERE id = ?""", 
                              args=(contract_id,))
    return res
    
def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * FROM contracts""",
                             many=True)
    return res

def new(contract: contracts) -> dict:
    res = db_manager.execute(query="""INSERT INTO contracts(event_id, model_id, payment) 
                                       VALUES(?, ?, ?) 
                                       RETURNING id""", 
                              args=(contract.event_id, contract.model_id, contract.payment))
    return res

def update(contract: contracts) -> dict:
    res = db_manager.execute(query="""UPDATE contracts 
                                        SET payment = ?
                                        WHERE id = ?""", 
                              args=(contract.payment, contract.id))
    return res

def delete(contract_id: int) -> dict:
    res = db_manager.execute(query="""DELETE FROM contracts WHERE id = ?""", 
                              args=(contract_id,))
    return res
