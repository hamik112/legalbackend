
from fastapi import FastAPI,Header,Request,Path,Query
from starlette.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
from app.core.logger import init_logging,logger
from app.routes.contact import contact_router
from app.routes.leads import lead_router
from app.routes.track import tracker_router
from app.routes.ccpa import ccpa_route
from app.routes.main import main_router
from app.db import database
from app.core.config import config

origins = ["https://entitledtojustice.com",'https://www.entitledtojustice.com','https://api.entitledtojustice.com']

app = FastAPI()


app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"], expose_headers=["*"])
init_logging()

app.add_middleware(ProxyHeadersMiddleware,trusted_hosts="*")




app.include_router(contact_router,prefix="/contactus")
app.include_router(lead_router,prefix="/lead")
app.include_router(tracker_router,prefix="/track")
app.include_router(ccpa_route,prefix="/ccpa")


app.state.database = database
init_logging()

@app.on_event("startup")
async def startup() -> None:
    database = app.state.database
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown() -> None:
    database = app.state.database
    if database.is_connected:
        await database.disconnect()


#app.include_router(main_router,prefix = "")
