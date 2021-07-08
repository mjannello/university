from flask import Flask

from db import db
from models.career import Career
from models.grade import GradesReport
from models.student import Student
from models.subject import Subject

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Futbol93.@localhost/university'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        subject = Subject(name='analisis matematico 2')
        student = Student(first_name='matias', last_name='jannello', university_id=96479)
        grades_report = GradesReport()
        career = Career(name='Ingeniería Electrónica')

        student.grades_report = grades_report
        student.careers.append(career)

        db.session.add(student)
        db.session.add(grades_report)
        db.session.add(subject)
        db.session.add(career)

        db.session.commit()
    app.run()
