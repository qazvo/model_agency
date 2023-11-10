from server.database.db_manager import db_manager

from server.models_db import roles

def get(role_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * FROM roles WHERE id = ?""", 
                              args=(role_id,))
    return res
    
def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * FROM roles""",
                             many=True)
    return res

def new(role: roles) -> dict:
    res = db_manager.execute(query="""INSERT INTO roles(id, name, permission) 
                                       VALUES(?, ?, ?) 
                                       RETURNING id""", 
                              args=(role.id, role.name, role.permission))
    return res

def update(role_id: int, new_permission: roles.permission) -> dict:
    res = db_manager.execute(query="""UPDATE roles
                                        SET permission = ?
                                        WHERE id = ?""", 
                              args=(new_permission, role_id))
    return res

def delete(role_id: int) -> dict:
    res = db_manager.execute(query="""DELETE * FROM roles WHERE id = ?""", 
                              args=(role_id,))
    return res