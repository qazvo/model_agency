from database.db_manager import db_manager
import settings as settings
import uvicorn
from fastapi import FastAPI
##from server.routers import administrators, contracts, countries, customer_organizations, events, models, roles, users
from routers import administrators
from fastapi.responses import RedirectResponse

app = FastAPI(title='model_agency')

app.include_router(administrators.administrators_router)
##app.include_router(contracts)
##app.include_router(countries)
##app.include_router(customer_organizations)
##app.include_router(events)
##app.include_router(models)
##app.include_router(roles)
##app.include_router(users)

@app.router.get('/')
def start_page() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == "__main__": 
    uvicorn.run(app='start_server:app', reload=True, host=settings.HOST, port=settings.PORT)
