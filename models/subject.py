import uuid


class Subject:
    def __init__(self, name, department):
        self.id = uuid.uuid4()
        self.name = name
        self.department = department
        self.state = None
        self.__is_available = False

    @property
    def is_available(self):
        return self.__is_available
