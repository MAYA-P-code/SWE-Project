class Professor:
    def __init__(self, pID: str, pname: str, password: str):
        self.pID = pID       
        self.pname = pname   
        self.password = password  
        
def view_all_registered_students(self, course_id: str):
      db = get_db()

      rows = db.execute( 
          "sql",
       (course_id, self.pID),
        ).fetchall()

students = [dict(row) for row in rows]

        return students
