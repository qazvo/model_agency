import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source/server/database")
sys.path.append("D:/Program/Programing/Projects/model_agency/source/server")

from database.db_manager import db_manager

from models_db import users

def get(user_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * FROM users WHERE id = ?""", 
                              args=(user_id,))
    return res
    
def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * FROM users""",
                             many=True)
    return res

def new(user: users) -> dict:
    res = db_manager.execute(query="""INSERT INTO users(id, login, password, customer_organization_id, administrator_id, role_id) 
                                       VALUES(?, ?, ?, ?, ?, ?) 
                                       RETURNING id""", 
                              args=(user.id, user.login, user.password, user.customer_organization_id, user.administrator_id, user.role_id))
    return res

def update(user: users) -> dict:
    res = db_manager.execute(query="""UPDATE users
                                        SET password = ?
                                        WHERE id = ?""", 
                              args=(user.password, user.id))
    return res

def delete(user_id: int) -> dict:
    res = db_manager.execute(query="""DELETE FROM users WHERE id = ?""", 
                              args=(user_id,))
    return res