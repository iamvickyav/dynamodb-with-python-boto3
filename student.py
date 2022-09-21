class Student:
    dept: str
    stud_id: str
    stud_name: str
    stud_age: int
    subjects: list

    def __init__(self, dept, stud_id, stud_name, stud_age, subjects):
        self.dept = dept
        self.stud_id = stud_id
        self.stud_name = stud_name
        self.stud_age = stud_age
        self.subjects = subjects
