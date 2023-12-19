from database.db_manager import db_manager
import settings
import uvicorn
from fastapi import FastAPI
from routers import administrators, contracts, countries, customer_organizations, events, models, roles, users
from fastapi.responses import RedirectResponse

app = FastAPI(title='model_agency')

app.include_router(administrators.administrators_router)
app.include_router(contracts.contracts_router)
app.include_router(countries.countries_router)
app.include_router(customer_organizations.customer_organizations_router)
app.include_router(events.events_router)
app.include_router(models.models_router)
app.include_router(roles.roles_router)
app.include_router(users.users_router)

@app.router.get('/')
def start_page() -> RedirectResponse:
    return RedirectResponse('/docs')

if __name__ == "__main__": 
    uvicorn.run(app='start_server:app', reload=True, host=settings.HOST, port=settings.PORT)
