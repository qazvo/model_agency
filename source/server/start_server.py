from server.database.db_manager import db_manager
import server.settings as settings, uvicorn
from fastapi import FastAPI
from server.routers import administrators
from fastapi.responses import RedirectResponse

app = FastAPI(title='model_agency')

app.include_router(administrators)

@app.router.get('/')
def start_page() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == "__main__": 
    uvicorn.run(app='start_server:app', reload=True, host=settings.HOST, port=settings.PORT)
