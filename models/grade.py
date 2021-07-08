import uuid

from sqlalchemy import CheckConstraint
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    grades_report_id = db.Column(UUID(as_uuid=True), db.ForeignKey('grades_reports.id'))
    subject_id = db.Column(UUID(as_uuid=True), db.ForeignKey('subjects.id'))
    mark = db.Column(db.Integer)
    file = db.Column(db.String(80))
    book = db.Column(db.String(80))
    approval_date = db.Column(db.Date)

    def __init__(self, subject, mark, approval_date, file, book):
        self.subject = subject
        self.mark = mark
        self.approval_date = approval_date
        self.file = file
        self.book = book


class GradesReport(db.Model):
    __tablename__ = 'grades_reports'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey('students.id'))  # 1 to 1 relationship
    grades = db.relationship('Grade', backref='grades_report')  # 1 to many relationship

    def __init__(self):
        self.grades = []
