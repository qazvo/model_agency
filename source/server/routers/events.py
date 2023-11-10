import fastapi

import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source")
sys.path.append("D:/Program/Programing/Projects/model_agency")

from source.server.models_db import events
from source.server.resolvers import events


events_router = fastapi.APIRouter(prefix='/events', tags=["Events"])


@events_router.get(path='/get/{event_id}', response_model=dict)
def get_event(event_id: int) -> dict:
    return events.get(event_id = event_id)

@events_router.get_all(path='/get', response_model=dict)
def get_events() -> dict:
    return events.get_all()

@events_router.new(path='/new/{event_id}', response_model=dict)
def new_event(event: events) -> dict:
    return events.new(event = event)

@events_router.put(path='/updateName/{event_id}', response_model=dict)
def update_name(event_id: int, new_name: events.name) -> dict:
    return events.get(event_id = event_id, new_name = new_name)

@events_router.delete(path='/delete/{event_id}', response_model=dict)
def delete_event(event_id: int) -> dict:
     return events.delete(event_id = event_id)