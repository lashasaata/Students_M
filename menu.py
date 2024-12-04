from services import Services

class Menu:
    def __init__(self):
        self.services = Services()
        self.menu = {
            "n": self.add_student,
            "d": self.delete_student,
            "a": self.show_students,
            "s": self.show_students,
            "u": self.change_grade
        }

    def commands(self):
        print('\n"X": Exit\n"N": Add student\n"D": Delete student\n"A": All students\n"S": Student by roll number\n"U": Update grade')

        command = ""

        while command not in ("x","n","a","s","u","d"):
            command = input("\nEnter command from the menu!.. ").lower()
        
        if command == "x":
            return command
        elif command == "s":
            self.show_students("s")
        else:
            self.menu[command]()
    
    def run(self):
        print("-----------------Student app is running------------------")

        def rp():
            if self.commands() == "x":
                print("Process ended...")
                return      
            else:
                return rp()
            
        rp()

    def add_student(self):
        print("\n-----------------Adding student------------------")

        first_name = input("What is the student's first name: ").strip().lower()

        while not first_name.isalpha():
            first_name = input("The student's firstname must be a string: ").strip().lower()

        last_name = input("What is the student's lastname: ").strip().lower()

        while not last_name.isalpha():
            last_name = input("The student's lastname must be a string: ").strip().lower()
        
        grade = input("Enter the student's grade: ").strip().lower()

        while grade not in ("a", "b", "c", "d", "e", "f"):
            grade = input('Student\'s grade must be one of these ["A","B","C","D","E","F"]: ').strip().lower()

        self.services.add_student(first_name,last_name,grade.upper())

    def delete_student(self):
        roll = input("Enter student's roll number: ")

        while not roll.isdigit():
            roll = input("Student's roll number must be an int type: ")

        self.services.delete_student(int(roll))


    def show_students(self, which=""):
        if which == "s":
            roll = input("Enter student's roll number: ")

            while not roll.isdigit():
                roll = input("Student's roll number must be an int type: ")
            
            result = self.services.show_students(int(roll))
        else:
            result = self.services.show_students()

        if len(result) > 0:
            print()
            print("=" * 40)
            print(f"{'Roll'.ljust(7)}{'Name'.ljust(25)}{'Grade'.ljust(25)}")
            print("-" * 40)

            for st in result:
                roll_number = str(st["roll_number"]).ljust(7)
                name = st["name"].ljust(25)
                grade = st["grade"].center(0)
                
                print(f"{roll_number}{name}{grade}")
                print("-"*40)
        else:
            print("\nStudent has not found!")

    def change_grade(self):
        roll = input("\nEnter student's roll number: ")

        while not roll.isdigit():
            roll = input("Student's roll number must be an int type: ")

        grade = input("Enter the student's new grade: ").strip().lower()

        while grade not in ("a", "b", "c", "d", "e", "f"):
            grade = input('Student\'s grade must be one of these: ["A","B","C","D","E","F"]').strip().lower()

        self.services.change_grade(int(roll), grade.upper())
