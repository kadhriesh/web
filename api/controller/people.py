
from fastapi import HTTPException, FastAPI, APIRouter
from typing import List, Optional
from bson import ObjectId
from api.utils.mongo_connection import MongoDBConnection
from api.model.people import People
from api.service.people import PeopleSvc


router = APIRouter()

@router.post("/people", response_model=People)
def create_People(People: People):
    service = PeopleSvc()
    id = service.add_people(people_data=People)
    return id

@router.get("/people", response_model=List[People])
def list_people():
    db = MongoDBConnection().get_database()
    people = list(db.people.find())
    return [p for p in people]

@router.get("/people/{People_id}", response_model=People)
def get_People(People_id: str):
    db = MongoDBConnection().get_database()
    People = db.people.find_one({"_id": ObjectId(People_id)})
    if not People:
        raise HTTPException(status_code=404, detail="People not found")
    return People

@router.put("/people/{People_id}", response_model=People)
def update_People(People_id: str, People: People):
    db = MongoDBConnection().get_database()
    update_data = People.dict(exclude_unset=True, by_alias=True)
    result = db.people.find_one_and_update(
        {"_id": ObjectId(People_id)},
        {"$set": update_data},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="People not found")
    return result

@router.delete("/people/{People_id}")
def delete_People(People_id: str):
    db = MongoDBConnection().get_database()
    result = db.people.delete_one({"_id": ObjectId(People_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="People not found")
    return {"detail": "People deleted"}
