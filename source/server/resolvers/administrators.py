import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source/server/database")
sys.path.append("D:/Program/Programing/Projects/model_agency/source/server")

from database.db_manager import db_manager

from models_db import administrators

def get(administrator_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * FROM administrators WHERE id = ?""", 
                              args=(administrator_id,))
    return res
    
def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * FROM administrators""",
                             many=True)
    return res

def new(administrator: administrators) -> dict:
    res = db_manager.execute(query="""INSERT INTO administrators(id, FIO, number_phone) 
                                       VALUES(?, ?, ?)
                                        RETURNING id""", 
                              args=(administrator.id, administrator.FIO, administrator.number_phone))
    return res

def update(administrator: administrators) -> dict:
    res = db_manager.execute(query="""UPDATE administrators 
                                        SET phone_number = ?
                                        WHERE id = ?""", 
                              args=(administrator.id, administrator.number_phone))
    return res

def delete(administrator_id: int) -> dict:
    res = db_manager.execute(query="""DELETE * FROM administrators WHERE id = ?""", 
                              args=(administrator_id,))
    return res
