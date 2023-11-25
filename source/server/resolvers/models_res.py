import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source/server/database")
sys.path.append("D:/Program/Programing/Projects/model_agency/source/server")

from database.db_manager import db_manager

from models_db import models

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

def update(model: models) -> dict:
    res = db_manager.execute(query="""UPDATE models
                                        SET number_phone = ?
                                        WHERE id = ?""", 
                              args=(model.number_phone, model.id))
    return res

def delete(model_id: int) -> dict:
    res = db_manager.execute(query="""DELETE FROM models WHERE id = ?""", 
                              args=(model_id,))
    return res