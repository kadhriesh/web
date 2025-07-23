from api.dao.base_dao import (
    BaseDao,
)


class PeopleDAO(BaseDao):

    def __init__(self):
        super().__init__()
        self.people_collection = self.getmongo_client["people"]

    def get_people_by_id(self, people_id):
        people = self.people_collection.find_one({"id": people_id})
        if not people:
            raise ValueError("No people found with the given ID")
        return people

    def get_people_list(self, page: int, page_size: int):
        try:
            people_list = (
                self.people_collection.find()
                .sort("name", 1)
                .skip((page - 1) * page_size)
                .limit(page_size)
            )
            if not people_list:
                raise ValueError("No people found")
            return list(people_list)
        except ValueError as e:
            raise ValueError("No people found")

    def save_people(self, people):
        try:
            people_id = self.people_collection.insert_one(people.dict())
            if not people_id:
                raise ValueError("Failed to create people")
            return people_id.inserted_id
        except Exception as e:
            raise ValueError("Failed to create people")

    def update_people(self, people_id, people_data):
        return self.people_collection.update(people_data)

    def delete_people(self, people_id):
        return self.people_collection.delete_one(people_id)
