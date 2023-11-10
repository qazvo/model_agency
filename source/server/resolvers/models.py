from server.database.db_manager import db_manager

from server.models_db import models

def get(model_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * FROM models WHERE id = ?""", 
                              args=(model_id,))
    return res
    
def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * FROM models""",
                             many=True)
    return res

def new(model: models) -> dict:
    res = db_manager.execute(query="""INSERT INTO models(id, FIO, gender, number_phone, height, weight) 
                                       VALUES(?, ?, ?, ?, ?, ?) 
                                       RETURNING id""", 
                              args=(model.id, model.FIO, model.gender, model.number_phone, model.height, model.weight))
    return res

def update(model_id: int, new_number_phone: models.number_phone) -> dict:
    res = db_manager.execute(query="""UPDATE models
                                        SET number_phone = ?
                                        WHERE id = ?""", 
                              args=(new_number_phone, model_id))
    return res

def delete(model_id: int) -> dict:
    res = db_manager.execute(query="""DELETE * FROM models WHERE id = ?""", 
                              args=(model_id,))
    return res