from abc import ABC, abstractmethod
import random
from patterns import Bridge


# Фабричный метод
class Student_Creator(ABC):

    @abstractmethod
    def create_student_list(self):
        pass

    @abstractmethod
    def create_student(self):
        """Фабричный метод"""
        pass


# Создатель объектов фабричного метода
class Second_Year_Creator(Student_Creator):
    def __init__(self):
        self.courseworks_list = ["DFACS","OS"]
        self.exams_list = ["NC","DWA","CT"]
        self.amount = 10

    def create_student(self):
        courseworks_dict = {}
        exams_dict = {}
        for x in self.courseworks_list:
            courseworks_dict[x] = random.randint(1, 5)
        for x in self.exams_list:
            exams_dict[x] = random.randint(1, 5)
        return Second_Year_Student(courseworks_dict, exams_dict)

    def create_student_list(self):
        students_list = []
        for i in range(self.amount):
            student = self.create_student()
            students_list.append(student)
        return students_list

# Другой создатель объектов фабричного метода
class First_Year_Creator(Student_Creator):
    def __init__(self, implementation):
        self.subjects_list = ["Math", "ODA", "Physical culture", "Ecology"]
        self.exams_list = ["physic", "chemistry"]
        self.amount = 10
        self.implementation = implementation

    def create_student(self):
        subj_dict = {}
        exams_dict = {}
        for x in self.subjects_list:
            subj_dict[x] = random.randint(1, 5)
        for x in self.exams_list:
            exams_dict[x] = random.randint(1, 5)
        implementation = self.implementation(subj_dict, exams_dict)
        return First_Year_Student(implementation)

    def create_student_list(self):
        students_list = []
        for i in range(self.amount):
            student = self.create_student()
            students_list.append(student)
        return students_list


# интерфейс объекта фабричного метода
class Student(ABC):
    def __init__(self):
        self.name = random.randint(0, 10000)

    def print_marks(self):
        print(self.name, "  ", self.get_marks())
        return ()

    @abstractmethod
    def get_marks(self) -> str:
        pass


# Объект фабричного метода+использует мост для реализации метода get marks
class First_Year_Student(Student):
    def __init__(self, implementation: Bridge.Implementation):
        super().__init__()
        self.implementation = implementation

    def get_marks(self):
        return self.implementation.get_marks()

# Другой объект фабричного метода
class Second_Year_Student(Student):
    def __init__(self, courseworks, exams):
        super().__init__()
        self.courseworks = courseworks
        self.exams = exams

    def get_marks(self):
        marks = 0
        marks_count = 0
        for x in self.courseworks.values():
            marks += x
        for x in self.exams.values():
            marks += x
        return marks
