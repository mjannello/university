from models.grade import GradesReport


class Student:
    def __init__(self, first_name, last_name, university_id):
        self.first_name = first_name
        self.last_name = last_name
        self.university_id = university_id
        self.careers = []
        self.report_card = GradesReport()
