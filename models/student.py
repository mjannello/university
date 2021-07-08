import uuid
import logging
from sqlalchemy.dialects.postgresql import UUID
from db import db


logger = logging.getLogger(__name__)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    university_id = db.Column(db.Integer(), nullable=False)
    grades_report = db.relationship('GradesReport', backref='student', uselist=False)  # 1 to 1 relationship

    @classmethod
    def find_by_id(cls, _id):
        logger.debug(f'Find product by id: {_id}')
        student = cls.query.get(_id)
        return student
