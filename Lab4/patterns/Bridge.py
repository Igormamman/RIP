from abc import ABC, abstractmethod

#интерфейс моста
class Implementation():
    def __init__(self, exams, subjects):
        self.subjects = subjects
        self.exams = exams

    @abstractmethod
    def get_marks(self):
        pass

#первый вариант реализации интерфейса моста
class First_Year_API_1(Implementation):

    def get_marks(self):
        marks = 0
        for x in self.subjects.values():
            marks += x
        for x in self.exams.values():
            marks += x
        return marks

#второй вариант реализации интерфейса
class First_Year_API_2(Implementation):

    def get_marks(self):
        marks = 0
        count = 0
        for x in self.subjects.values():
            marks += x
            count += 1
        for x in self.exams.values():
            marks += x
            count += 1
        return marks / count