class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def introduce(self):
        return f"My name is {self.__name} and I am {self.__age} years old."


class Student(Person):
    def __init__(self, name="Placeholder Name", age=0, grade="none"):
        super().__init__(name, age)
        self.__grade = grade
        self.__courses = []  # List of enrolled courses

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def introduce(self):
        return f"{super().introduce()} Studying in {self.__grade}th grade."

    def enroll_course(self, course):
        self.__courses.append(course)

    def list_courses(self):
        return [course.get_course_name() for course in self.__courses]


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_subject(self):
        return self.__subject

    def introduce(self):
        return f"{super().introduce()} Teaching {self.__subject}."


class Admin(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.__department = department

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.__department

    def introduce(self):
        return f"{super().introduce()} Working in {self.__department} Department."


class Courses:
    def __init__(self, course_name, grade, teacher):
        self.__course_name = course_name
        self.__grade = grade
        self.__teacher = teacher

    def set_course_name(self, course_name):
        self.__course_name = course_name

    def get_course_name(self):
        return self.__course_name

    def set_teacher(self, teacher):
        self.__teacher = teacher

    def get_teacher(self):
        return self.__teacher

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def __str__(self):
        return f"Course: {self.__course_name}, Grade: {self.__grade}, Teacher: {self.__teacher.get_name()}"


# Example Usage
students = [
    Student("Utkarsh", 22, 12),
    Student("Sohan", 19, 10)
]

teachers = [
    Teacher("Mohan", 43, "Science"),
    Teacher("Rajesh", 34, "Maths")
]

courses = [
    Courses("Physics", 12, teachers[0]),
    Courses("Mathematics", 10, teachers[1])
]

students[0].enroll_course(courses[0])
students[1].enroll_course(courses[1])

# Print student information and their enrolled courses
for student in students:
    print(student.introduce())
    print("Enrolled in:", student.list_courses())

# Print admin information
admin = Admin("Prem", 30, "Admission Committee")
print(admin.introduce())
