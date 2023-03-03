import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number, visibility
from problem3 import lab_location

class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(0.8)
    @number('3.1')
    def test1(self):
        '''Test [100, 90, 85] + [85] * 355 + [90, 98]'''

        case_input = [100, 90, 85] + [85] * 355 + [90, 98]
        case_output = 0
        assert lab_location(case_input) == case_output

    @weight(0.8)
    @number('3.2')
    def test2(self):
        '''Test [70] * 4 + [70, 80, 90, 89, 70, 20, 70] + [70] * 349'''
        case_input = [70] * 4 + [70, 80, 90, 89, 70, 20, 70] + [70] * 349
        case_output = 7
        assert lab_location(case_input) == case_output

    @weight(0.8)
    @number('3.3')
    def test3(self):
        '''Test [0] * 60 + list(range(200)) + [800, 900, 1000, 900, 0] + [40] * 95'''
        case_input = [0] * 60 + list(range(200)) + [800, 900, 1000, 900, 0] + [40] * 95
        case_output = 263
        assert lab_location(case_input) == case_output

    @weight(0.8)
    @number('3.4')
    def test4(self):
        '''Test [0, 115, 20, 9, 80, 10] + [4] * 353 + [200]'''
        case_input = [0, 115, 20, 9, 80, 10] + [4] * 353 + [200]
        case_output = 359
        assert lab_location(case_input) == case_output


    @weight(0.8)
    @number('3.5')
    def test5(self):
        '''Secret Test'''
        case_input = [0, 100, 20, 200, 80, 10] + [5] * 354
        case_output = 3
        assert lab_location(case_input) == case_output

