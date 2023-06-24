import uuid

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    total_student_count = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_student_count += 1

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        print("Student ID: ", self.student_id)
        print("Student Name: ", self.student_name)
        print("Student Age: ", self.student_age)
        print("Student Number: ", self.student_number)

    def get_student_courses(self):
        for course in self.courses_list:
            print("Course: {}, Mark: {}".format(course.course_name, course.course_mark))

    def get_student_average(self):
        if len(self.courses_list) == 0:
            return 0.0

        total_marks = sum(float(course.course_mark) for course in self.courses_list)
        return total_marks / len(self.courses_list)

students_list = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")

        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        student = Student(student_name,student_age,student_number)
        students_list.append(student)

        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students_list:
            if student.student_number == student_number:
                students_list.remove(student)
                found = True
                break

        if found:
            print("Student Deleted Successfully")
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students_list:
            if student_number == student_number:
                print(student.get_student_details())
                found = True
                break

        if not found:
            print("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students_list:
            if student_number == student_number:
                print("Student Average: {}".format(student.get_student_average()))
                found = True
                break

        if not found:
            print("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number: ")
        found = False

        for student in students_list:
            if student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = input("Enter Course Mark: ")
                course = Course(course_name,course_mark)
                student.enroll_course(course)
                found = True
                break

        if not found:
            print("Student Not Exist")
    elif selection == 6:
      break

    else:
        print("Invalid selection. Please choose a valid option.")