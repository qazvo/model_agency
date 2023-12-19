import fastapi

from models_db import events
from resolvers import events_res


events_router = fastapi.APIRouter(prefix='/events', tags=["Events"])


@events_router.get(path='/get/{event_id}', response_model=dict)
def get_event(event_id: int) -> dict:
    return events_res.get(event_id = event_id)

@events_router.get(path='/get', response_model=dict)
def get_events() -> dict:
    return events_res.get_all()

@events_router.post(path='/new', response_model=dict)
def new_event(event: events) -> dict:
    return events_res.new(event = event)

@events_router.put(path='/updateName/{event_id}', response_model=dict)
def update_name(event: events) -> dict:
    return events_res.update(event = event)

@events_router.delete(path='/delete/{event_id}', response_model=dict)
def delete_event(event_id: int) -> dict:
     return events_res.delete(event_id = event_id)