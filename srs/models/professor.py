class Professor:
    def __init__(self, pID: str, pname: str, password: str):
        self.pID = pID       
        self.pname = pname   
        self.password = password  

def view_all_registered_students(
        self,
        course_id: str,
        courses: list,
        registrations: list,
        students: list,
    ):

course_found = False
        for course in courses:
            if course["cID"] == course_id and course["PrID"] == self.pID:
                course_found = True
                break
        if not course_found:
            return[]

registered_student_ids = [
            reg["stuID"]
            for reg in registrations
            if reg["coID"] == course_id
        ]

students_by_id = {stu["stID"]: stu for stu in students}

 result = []
        for sid in registered_student_ids:
            if sid in students_by_id:
                result.append(students_by_id[sid])

        return result
