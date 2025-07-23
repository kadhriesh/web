from typing import (
    List,
    Optional,
)

from bson import (
    ObjectId,
)
from fastapi import (
    APIRouter,
    HTTPException,
)
from fastapi.responses import JSONResponse

from api.model.people import (
    People,
)
from api.service.people import (
    PeopleSvc,
)
from api.utils.mongo_connection import (
    MongoDBConnection,
)

router = APIRouter()


@router.post("/people", status_code=201)
def create_people(people: People):
    try:
        service = PeopleSvc()
        people_id = service.save_people(people_data=people)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return JSONResponse(
        status_code=201, content={"id": str(people_id) + " created successfully"}
    )


@router.get("/people", response_model=List[People])
def list_people(page: Optional[int] = 1, page_size: Optional[int] = 10):
    try:
        service = PeopleSvc()
        people_list = service.get_people_list(page, page_size)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return people_list


@router.get("/people/{people_id}", response_model=People)
def get_people(people_id: int):
    try:
        service = PeopleSvc()
        people = service.get_people_by_id(people_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return people


@router.put("/people/{people_id}", response_model=People)
def update_people(people_id: str, people: People):
    try:
        service = PeopleSvc()
        people = service.update_people(people_id, people)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return people


@router.delete("/people/{People_id}")
def delete_people(people_id: str):
    db = MongoDBConnection().get_database()
    result = db.people.delete_one({"_id": ObjectId(people_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="People not found")
    return {"detail": "People deleted"}
