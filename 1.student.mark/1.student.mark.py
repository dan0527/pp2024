from math import *

def studentInfor():
    student = {}
    student['id'] = input("Enter student name: ")
    student['name'] = input("Enter student ID: ")
    student['dob'] = input("Enter student DoB: ")
    return student


def courses():
    course = {}
    course['id'] = input("Enter course ID: ")
    course['name'] = input("Enter course name: ")
    return course


def fillMark(studentList, courseList):
    courseId = input("Enter the course ID to enter marks for: ")
    for student in studentList:
        marks = float(input(f"Enter marks for student {student['name']} in course {courseId}: "))
        student.setdefault('marks', {})[courseId] = marks


def listCourses(courseList):
    print("Courses:")
    for course in courseList:
        print("ID:", course['id'])
        print("Name:", course['name'])
        print()


def listStudents(studentList):
    print("Students:")
    for student in studentList:
        print("Name:", student['name'])
        print("ID:", student['id'])
        print()


def showMarkOfStudent(studentList, courseId):
    print(f"Marks of students in course {courseId}:")
    for student in studentList:
        if 'marks' in student and courseId in student['marks']:
            marks = student['marks'][courseId]
            print("ID:", student['id'])
            print("Name:", student['name'])
            print("Marks:", marks)
            print()


def main():
    numStudent = int(input("Enter the number of students: "))

    studentList = []
    for _ in range(numStudent):
        student = studentInfor()
        studentList.append(student)

    numCourse = int(input("Enter the number of courses: "))

    courseList = []
    for _ in range(numCourse):
        course = courses()
        courseList.append(course)

    fillMark(studentList, courseList)

    print("\n--- Options ---")
    print("1. List of courses")
    print("2. List of students")
    print("3. Show marks of students in a course")

    option = int(input("Choose option: "))

    if option == 1:
        listCourses(courseList)
    elif option == 2:
        listStudents(studentList)
    elif option == 3:
        courseId = input("Enter the course ID: ")
        showMarkOfStudent(studentList, courseId)
    else:
        print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()


