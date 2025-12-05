from flask import Blueprint, render_template
from professor import Professor

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

@professor_bp.route("/<p_id>/courses/<c_id>/students")
def view_all_registered_students(p_id, c_id):
    prof = Professor(pID=p_id, pname="", password="")
    students = prof.view_all_registered_students(c_id)
    return render_template(
        "professor_students.html",
        professor=prof,
        course_id=c_id,
        students=students,
    )
