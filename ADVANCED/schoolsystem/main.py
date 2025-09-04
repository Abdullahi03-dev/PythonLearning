class Student:
    def __init__(self, student_id, name, age, school_class):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.school_class = school_class
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def display_info(self):
        return {
            "ID": self.student_id,
            "Name": self.name,
            "Age": self.age,
            "Class": self.school_class,
            "Courses": self.courses
        }


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        if not self.students:
            print("No students found.")
        for s in self.students:
            print(s.display_info())

    def assign_course(self, student_id, course):
        for s in self.students:
            if s.student_id == student_id:
                s.enroll_course(course)
                print(f"Course '{course}' added to {s.name}")
                return
        print("Student not found!")


# -------- Main Program --------
school = School()

while True:
    print("\n--- School Management Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Assign Course to Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        clas = input("Enter Class: ")
        student = Student(sid, name, age, clas)
        school.add_student(student)
        print("Student added successfully!")

    elif choice == "2":
        school.view_students()

    elif choice == "3":
        sid = input("Enter Student ID: ")
        course = input("Enter Course: ")
        school.assign_course(sid, course)

    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again!")