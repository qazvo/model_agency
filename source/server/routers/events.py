import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from models_db import events
from resolvers import events


events_router = fastapi.APIRouter(prefix='/events', tags=["Events"])


@events_router.get(path='/get/{event_id}', response_model=dict)
def get_event(event_id: int) -> dict:
    return events.get(event_id = event_id)

@events_router.get(path='/get', response_model=dict)
def get_events() -> dict:
    return events.get_all()

@events_router.post(path='/new', response_model=dict)
def new_event(event: events) -> dict:
    return events.new(event = event)

@events_router.put(path='/updateName/{event_id}', response_model=dict)
def update_name(event: events) -> dict:
    return events.get(event = event)

@events_router.delete(path='/delete/{event_id}', response_model=dict)
def delete_event(event_id: int) -> dict:
     return events.delete(event_id = event_id)