class professor :

  def__init__ (self . professor_id: int , name : str , password:str ):
  self.if = professor_id
  self.name = name 
  self.password = password 

def_teaches_course (self, course_id : int, courses: list[dict] ) -> bool:

for course in courses:
  if course ["id"] == course_id and course ["professor_id"]== self.id:
    return true 
return false 

def view_registered_students(
  self,
  course_id :int ,
  courses: list [dict],
  registrations :list [dict]
  students : list [dict]
) -> list [dict]:

if not self._teaches_course(course_id, courses):
  return []

student_ids= [
  reg["student_id"]
  for reg in registrations 
  if reg["course_id"] == course_id 
]
students_by_id = {s["id"]: s for s in students}
return [ students_by_id[sid] for sid in student_ids if sid in students_by_id ]

def admit_students 
(
  self,
  student_id: int,
        course_id: int,
        courses: List[Dict],
        registrations: List[Dict],
    ) -> bool: 

if not self._teaches_course (course_id, courses) :
  return false 
for reg in registrations:
  if reg["course_id"] == course_id and reg["students_id"] == student_id:
    return false 

course = next ((c for c in courses id c ["id"] == course_id ) , none)
if course is none :
  return false 

current_counts = sum (
  1 for reg in registrations if reg [ "course_id" ] == course_id
)
if currents_counts >= course["capacity"]:
  return false 

registration.append(
  {
    "student_id" : student_id,
    "course_id" : course_id,
    "grade" : none,
  }
)
return true 

def remove_student(
   self,
        student_id: int,
        course_id: int,
        courses: List[Dict],
        registrations: List[Dict],
    ) -> bool:

  if not self._teaches_course(course_id , courses):
    return false 

for index , reg in enumerate(registrations):
  if reg [ "course_id"] == course_id and reg["student_id"] == student_id :
    registrations.pop {index) 
return true 
return false 

 def assign_grade(
        self,
        student_id: int,
        course_id: int,
        letter_grade: str,
        courses: List[Dict],
        registrations: List[Dict],
        valid_grades: Optional[List[str]] = None,
    ) -> bool:

        if not self._teaches_course(course_id, courses):
            return False

        grade = letter_grade.strip().upper()
if valid_grades is not None and grade not in valid_grades:
            return False

  for reg in registrations:
            if reg["course_id"] == course_id and reg["student_id"] == student_id:
                reg["grade"] = grade
                return True
return false 

 def change_password(self, old_password: str, new_password: str) -> bool:
 if self.password != old_password:
            return False
        self.password = new_password
        return True

 def check_password(self, password: str) -> bool:
   return self.password == password 
