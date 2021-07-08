from flask import jsonify
from flask_restplus import Resource
from sqlalchemy.exc import SQLAlchemyError

from api import api

from models.student import Student

ns_students = api.namespace('students', description='Student Resource')


@ns_students.route('/<student_id>')
class StudentsCollection(Resource):
    def get(self, student_id):
        try:
            student = Student.find_by_id(student_id)
            if student:
                return jsonify({'id': student.id,
                                "name": student.first_name
                                })
            return f'Student with id {student_id} not found', 404
        except SQLAlchemyError:
            return f'An exception occurred while retrieving product {student_id}', 500
