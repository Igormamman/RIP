import random
from patterns import Bridge, Fabric_Method, iterator
import unittest
import unittest.mock
from unittest.mock import patch
from unittest import TestCase

class TestPatterns(TestCase):
    def setUp(self):
        self.first_year_creator = Fabric_Method.First_Year_Creator(Fabric_Method.Bridge.First_Year_API_2)
        self.first_year_studs = self.first_year_creator.create_student_list()

#используем TDD+Mock
    @patch('patterns.Fabric_Method.Second_Year_Student')
    def test_fabric(self,mock_student):
        self.first_year_creator = Fabric_Method.First_Year_Creator(Fabric_Method.Bridge.First_Year_API_2)
        self.first_year_studs = self.first_year_creator.create_student_list()
        for x in self.first_year_studs:
            assert 0 <= x.get_marks() <= 5
        second_year_student=mock_student
        second_year_student.get_marks().return_value=random.randint(-5,-1)
        assert -10<second_year_student.get_marks().return_value<0

    def test_iterator(self):
        first_year_creator = Fabric_Method.First_Year_Creator(Fabric_Method.Bridge.First_Year_API_2)
        first_year_studs = first_year_creator.create_student_list()
        iteration_list=list(iterator.Student_Iterator(first_year_studs))
        for x in range(len(iteration_list)-1):
            assert iteration_list[x].get_marks()<=iteration_list[x+1].get_marks()
#используем BDD



if __name__ == '__main__':
    unittest.main()

