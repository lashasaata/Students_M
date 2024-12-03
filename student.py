class Student:
    __id = 1
    def __init__(self, name: str, grade: str, roll: int = 0):
        self.id = Student.__id
        self.name = name
        self.roll_number = roll
        self.grade = grade

        Student.__id += 1

    def to_dict(self):
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "grade": self.grade
        }