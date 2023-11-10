from server.database.db_manager import db_manager

from server.models_db import administrators

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

def update(administrator_id: int, new_number_phone: administrators.number_phone) -> dict:
    res = db_manager.execute(query="""UPDATE administrators 
                                        SET phone_number = ?
                                        WHERE id = ?""", 
                              args=(new_number_phone, administrator_id))
    return res

def delete(administrator_id: int) -> dict:
    res = db_manager.execute(query="""DELETE * FROM administrators WHERE id = ?""", 
                              args=(administrator_id,))
    return res
