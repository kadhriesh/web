from api.dao.base_dao import BaseDao


class PeopleDAO(BaseDao):

    def __init__(self):
        super().__init__()

    def get_people(self,people):
        return id.inserted_id

    def get_people_by_id(self, people_id):
        return self.db.get_people_by_id(people_id)

    def add_people(self, people):
        try:
            db = self.getmongo_client
            id = db.people.insert_one(people)
            return id.inserted_id
        except (Exception) as e:
            raise e()

    def update_people(self, people_id, people_data):
        return self.db.update_people(people_id, people_data)

    def delete_people(self, people_id):
        return self.db.delete_people(people_id)