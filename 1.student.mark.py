class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        num_students = int(input("enter number of students: "))
        for _ in range(num_students):
            self.input_student_information()

    def input_student_information(self):
        student_id = input("student ID: ")
        name = input("student name: ")
        dob = input("student DoB: ")
        student = Student(student_id, name, dob)
        self.students.append(student)

    def input_number_of_courses(self):
        num_courses = int(input("enter number of courses: "))
        for _ in range(num_courses):
            self.input_course_information()

    def input_course_information(self):
        course_id = input("course ID: ")
        name = input("course name: ")
        course = Course(course_id, name)
        self.courses.append(course)

    def select_course_and_input_marks(self):
        course_id = input("enter course ID to input marks: ")
        for student in self.students:
            mark = float(input(f"mark of student {student.name} (ID: {student.student_id}): "))
            student.marks[course_id] = mark

    def list_courses(self):
        print("courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, name: {course.name}")

    def list_students(self):
        print("students:")
        for student in self.students:
            print(f"ID: {student.student_id}, name: {student.name}, DoB: {student.dob}")

    def show_student_marks_for_course(self):
        course_id = input("enter course ID to show marks: ")
        print(f"marks for course ID {course_id}:")
        for student in self.students:
            if course_id in student.marks:
                print(f"student ID: {student.student_id}, name: {student.name}, mark: {student.marks[course_id]}")

if __name__ == "__main__":
    school = School()
    school.input_number_of_students()
    school.input_number_of_courses()
    school.select_course_and_input_marks()
    school.list_courses()
    school.list_students()
    school.show_student_marks_for_course()