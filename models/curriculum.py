from models.subject import Subject


class Curriculum:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.subjects = []


class CurriculumSubject(Subject):
    def __init__(self, name, department, code, credits_points, correlatives, mandatory):
        super(CurriculumSubject, self).__init__(name, department)
        self.code = code
        self.credits_points = credits_points
        self.correlatives = correlatives
        self.mandatory = mandatory
