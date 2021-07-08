from db import db


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    university_id = db.Column(db.Integer(), nullable=False)
    careers = []
    report_card = db.relationship('GradesReport', back_populates='student')

