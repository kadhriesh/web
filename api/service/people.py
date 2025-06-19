from api.dao.people import PeopleDAO


class PeopleSvc:

    def __init__(self):
        pass


    def get_people(self):
        return self.people_dao.get_people()

    def get_people(self, people_id):
        return self.people_dao.get_people(people_id)

    def add_people(self, people_data):
        people_dao = PeopleDAO()
        return people_dao.add_people(people_data)

    def update_people(self, people_id, people_data):
        return self.people_dao.update_people(people_id, people_data)

    def delete_people(self, people_id):
        return self.people_dao.delete_people(people_id)