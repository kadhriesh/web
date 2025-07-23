from fastapi import (
    FastAPI,
)

from api.controller.people import (
    router as people_router,
)

app = FastAPI()
app.include_router(people_router)


# def bootstrap():
#     uvicorn.run(app, host="localhost")


# if __name__ == "__main__":
#     # bootstrap()
#     uvicorn.run(
#         "bootstrap:app",
#         host="localhost",
#         port=8080,
#     )
