import uvicorn
from api.controller.people import router as people_router
from api.controller.employee import router as employee_router
from fastapi import APIRouter, FastAPI

app = FastAPI()
app.include_router(people_router)
app.include_router(employee_router)

def bootstrap():
    uvicorn.run(app, host="localhost")

if __name__ == "__main__":
    bootstrap()