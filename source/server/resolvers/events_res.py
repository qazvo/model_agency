import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source/server/database")
sys.path.append("D:/Program/Programing/Projects/model_agency/source/server")

from database.db_manager import db_manager

from models_db import events

def get(event_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * FROM events WHERE id = ?""", 
                              args=(event_id,))
    return res
    
def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * FROM events""",
                             many=True)
    return res

def new(event: events) -> dict:
    res = db_manager.execute(query="""INSERT INTO events(id, name, country_id, customer_organization_id, date) 
                                       VALUES(?, ?, ?, ?, ?) 
                                       RETURNING id""", 
                              args=(event.id, event.name, event.country_id, event.customer_organization_id, event.date))
    return res

def update(event: events) -> dict:
    res = db_manager.execute(query="""UPDATE events
                                        SET name = ?
                                        WHERE id = ?""", 
                              args=(event.name, event.id))
    return res

def delete(event_id: int) -> dict:
    res = db_manager.execute(query="""DELETE FROM events WHERE id = ?""", 
                              args=(event_id,))
    return res