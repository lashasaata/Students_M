from student import Student
import os, json

class Services:
    def __init__(self):
        self.__students: dict[str, Student] = {}
        self.__read_data()

    def path(self):
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)

        file_path = os.path.join(script_dir, "data.json")
        return file_path

    def __read_data(self):
        try:
            with open(self.path(), mode="r", encoding="utf-8") as file:
                data = json.load(file)
            
            for id,s in data.items():
                self.__students[id] = Student(s["name"], s["grade"], s["roll_number"])

        except json.JSONDecodeError:
            self.__students = {}

    def __update_db(self):
        newdata = {}

        for id,s in self.__students.items():
            newdata[id] = s.to_dict()

        with open(self.path(), mode="w", encoding="utf-8") as file:
            json.dump(newdata, file, indent=4)
        
    
    def __update_roll(self):
        students = [s.to_dict() for s in self.__students.values()]

        students = sorted(students, key=lambda obj: obj["name"])

        update_sts = {}

        for index, st in enumerate(students):
            roll_number = index + 1
            update_sts[roll_number] = Student(st["name"], st["grade"], roll_number)

        return update_sts

    def add_student(self, first, last, grade):
        name = last.capitalize() + " " + first.capitalize()
        newstudent = Student(name, grade)
        self.__students[newstudent.id] = newstudent

        self.__students = self.__update_roll()
        self.__update_db()
        print("Student has successfully added!")
    
    def delete_student(self, roll):
        for id,st in self.__students.items():
            if st.roll_number == roll:
                del self.__students[id]

                self.__students = self.__update_roll()
                self.__update_db()

                print("Student has removed.")
                return
        else:
            print(f"Student with roll number-{roll} does not exist!")

    def show_students(self, roll=0):
        students = []

        if roll == 0:
            for id,st in self.__students.items():
                students.append(st.to_dict())
            
            return students
        else:
            for id,st in self.__students.items():
                if st.roll_number == roll:
                    students.append(st.to_dict())

                    return students
            else:
                return students
            
    def change_grade(self, roll, grade):
        for st in self.__students.values():
            if st.roll_number == roll:
                st.grade = grade
                self.__update_db()
                
                print("Grade has changed.")
                return
        else:
            print("Student has not found!")