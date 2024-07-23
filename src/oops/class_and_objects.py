from abc import ABC, abstractmethod

# Custom Exceptions
class InvalidAgeError(Exception):
    pass

class InvalidGradeError(Exception):
    pass

# Abstract Class
class Person(ABC):
    _total_persons = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person._total_persons += 1

    @abstractmethod
    def introduce(self):
        return f"Hello, my name is {self.__name} and I am {self.__age} years old."

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise InvalidAgeError("Age cannot be negative")
        self.__age = age
        

    @staticmethod
    def total_persons():
        return Person._total_persons

    @classmethod
    def increment_total(cls):
        cls._total_persons += 1

# Interface for common behavior
class Role(ABC):
    @abstractmethod
    def get_role(self):
        pass

# Student Class
class Student(Person, Role):
    def __init__(self, name="Placeholder Name", age=0, grade="none"):
        super().__init__(name, age)
        self.set_grade(grade)
        self.__courses = []

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if grade not in ["none", "A", "B", "C", "D", "F"]:
            raise InvalidGradeError("Invalid grade")
        self.__grade = grade

    def introduce(self):
        return f"{super().introduce()} Studying in {self.__grade}th grade."

    def enroll_course(self, course):
        self.__courses.append(course)

    def list_courses(self):
        return [course.get_course_name() for course in self.__courses]

    def get_role(self):
        return "Student"

# Teacher Class
class Teacher(Person, Role):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_subject(self):
        return self.__subject

    def introduce(self):
        return f"{super().introduce()} Teaching {self.__subject}."

    def get_role(self):
        return "Teacher"

# Admin Class
class Admin(Person, Role):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.__department = department

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.__department

    def introduce(self):
        return f"{super().introduce()} Working in {self.__department} Department."

    def get_role(self):
        return "Admin"

# Courses Class
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
    Student("Utkarsh", 22, "A"),
    Student("Sohan", 19, "B")
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



