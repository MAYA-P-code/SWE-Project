from flask import Blueprint, render_template, session, request
from srs.models.professor import Professor
from srs.repositories.professorRepo import professorRepo
from srs.db import get_db 

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

@professor_bp.route("/courses/<c_id>/students")
def get_students_in_course(c_id):
    p_id = session["userID"]
    p_name = session.get("username", "")
    db = get_db()
    repo = professorRepo(db, p_id) 

    prof = Professor(pID=p_id, pname=p_name, password="")
    students = repo.get_students_in_course(c_id)
    return render_template(
        "view_students.html",
        professor=prof,
        course_id=c_id,
        students=students,
    )
@professor_bp.route("/assign_grade", methods=["POST"])
def assign_grade():
    professor_id = session.get('userID')
    if not professor_id:
        return "Not logged in"
    
    student_id = request.form.get("student_id")
    course_id = request.form.get("course_id")
    grade = request.form.get("grade")
    
    db = get_db()
    repo = professorRepo(db, professor_id)
    result = repo.assign_grade(student_id, course_id, grade)


    return result
