from api.dao.people import (
    PeopleDAO,
)

from api.model.people import People


class PeopleSvc:

    def __init__(self):
        self.people_dao = PeopleDAO()

    def get_people_list(self, page: int, page_size: int):
        try:
            if page < 1 or page_size < 1:
                raise ValueError("Page and page size must be greater than 0")
            people_list = self.people_dao.get_people_list(page, page_size)
            return people_list
        except ValueError as e:
            raise ValueError("No people found") from e

    def get_people_by_id(self, people_id: int):
        try:
            people = self.people_dao.get_people_by_id(people_id)
            return people
        except ValueError:
            raise ValueError("Invalid People ID format")

    def save_people(self, people_data: People):
        try:
            return self.people_dao.save_people(people_data)
        except ValueError as e:
            raise ValueError("Failed to create people") from e

    def update_people(self, people_id, people_data):
        return self.people_dao.update_people(people_id, people_data)

    def delete_people(self, people_id):
        return self.people_dao.delete_people(people_id)
