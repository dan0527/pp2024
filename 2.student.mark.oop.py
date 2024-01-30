class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def enter_marks(self, course_id, marks):
        self.marks[course_id] = marks


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name


class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB: ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            self.courses.append(course)

    def input_marks(self):
        course_id = input("Enter the course ID to enter marks for: ")
        for student in self.students:
            marks = float(input(f"Enter marks for student {student.name} in course {course_id}: "))
            student.enter_marks(course_id, marks)

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print("ID:", course.id)
            print("Name:", course.name)
            print()

    def list_students(self):
        print("Students:")
        for student in self.students:
            print("Name:", student.name)
            print("ID:", student.id)
            print()

    def show_marks_of_students(self, course_id):
        print(f"Marks of students in course {course_id}:")
        for student in self.students:
            if course_id in student.marks:
                marks = student.marks[course_id]
                print("ID:", student.id)
                print("Name:", student.name)
                print("Marks:", marks)
                print()

    
    
if __name__ == '__main__':
    school_system = SchoolManagementSystem()
    school_system.input_students()
    school_system.input_courses()
    school_system.input_marks()
    school_system.list_courses()
    school_system.list_students()
    school_system.show_marks_of_students()
