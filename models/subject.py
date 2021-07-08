import uuid

from sqlalchemy.dialects.postgresql import UUID

from db import db


class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), nullable=False)
    grade = db.relationship('Grade', backref='subject', uselist=False)  # 1 to 1 relationship

    def __init__(self, name, department=None):
        self.id = uuid.uuid4()
        self.name = name
        self.department = department
        self.state = None
        self.__is_available = False

    @property
    def is_available(self):
        return self.__is_available
