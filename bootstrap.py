import uvicorn
from fastapi import FastAPI

from api.controller import router
from api.controller import employee,people


def bootstrap():
    # app.include_router(employee, prefix="/api/v1", tags=["v1"])
    # app.include_router(people, prefix="/api/v1", tags=["v1"])
    app = FastAPI()
    app.include_router(router)
    uvicorn.run(app, host="localhost")

