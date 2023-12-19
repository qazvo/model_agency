from database.db_manager import db_manager

from models_db import countries

def get(country_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * FROM countries WHERE id = ?""", 
                              args=(country_id,))
    return res
    
def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * FROM countries""",
                             many=True)
    return res

def new(country: countries) -> dict:
    res = db_manager.execute(query="""INSERT INTO countries(shortname, name) 
                                       VALUES(?, ?) 
                                       RETURNING id""", 
                              args=(country.shortname, country.name))
    return res

def update(country: countries) -> dict:
    res = db_manager.execute(query="""UPDATE countries 
                                        SET name = ?
                                        WHERE id = ?""", 
                              args=(country.name, country.id))
    return res

def delete(country_id: int) -> dict:
    res = db_manager.execute(query="""DELETE FROM countries WHERE id = ?""", 
                              args=(country_id,))
    return res