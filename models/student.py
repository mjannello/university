import uuid

from sqlalchemy.dialects.postgresql import UUID

from db import db


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    university_id = db.Column(db.Integer(), nullable=False)
    grades_report = db.relationship('GradesReport', backref='student', uselist=False)  # 1 to 1 relationship
