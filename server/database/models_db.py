from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class models(BaseModel):
    id : int
    FIO : str
    gender : str
    phone : str
    height : int
    weight : int

class countries(BaseModel):
    id : int
    shortname : str
    name : str 

class customer_organizations(BaseModel):
    id : int
    name : str 
    country_id : int
    contact_details : str
    inn : int
    confirmed : Optional[bool] = False

class events(BaseModel):
    id : int
    name : str 
    country_id : int
    customer_organization_id : int 
    date : datetime.date
    time : datetime.time 

class contracts(BaseModel):
    id : int
    event_id : int 
    model_id : int
    payment : float

class administrators(BaseModel):
    id : int
    FIO : str
    number_phone : str

class roles(BaseModel):
    id : int
    name : str
    permission : str

class users(BaseModel):
    id : int
    login : str
    password : str
    customer_organization_id : int 
    administrator_id : int
    role_id : int
