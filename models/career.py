import uuid

from sqlalchemy.dialects.postgresql import UUID

from db import db


# join table to relate students and careers (many to many)
students = db.Table('students_careers',
                    db.Column('student_id', db.ForeignKey('students.id')),
                    db.Column('career_id', db.ForeignKey('careers.id'))
                    )


class Career(db.Model):
    __tablename__ = 'careers'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), nullable=False)
    students = db.relationship(
        'Student', secondary=students, backref='careers'
    )  # many to many relationship

    def __init__(self, name):
        self.name = name
        self.curriculums = []
