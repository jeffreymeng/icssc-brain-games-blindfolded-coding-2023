import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number, visibility
from problem4 import find_lock_solutions


class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(0.8)
    @number('4.1')
    def test1(self):
        '''Test [0, 2, 3, 4, "END", 5, 6, 7, 8, 9]'''

        case_input = [0, 2, 3, 4, "END", 5, 6, 7, 8, 9]
        case_output = ["1234"]
        assert sorted(find_lock_solutions(case_input)) == case_output

    @weight(0.8)
    @number('4.2')
    def test2(self):
        '''Test [2, "END", 3, 1, 4, 3, 8, 2, 9, "END"]'''
        case_input = [2, "END", 3, 1, 4, 3, 8, 2, 9, "END"]
        case_output = ["0231", "7231"]
        assert sorted(find_lock_solutions(case_input)) == case_output

    @weight(0.8)
    @number('4.3')
    def test3(self):
        '''Test [3, 2, 5, 4, 6, 9, "END", 3, "END", "END"]'''
        case_input = [3, 2, 5, 4, 6, 9, "END", 3, "END", "END"]
        case_output = ['0346', '1259', '7346']
        assert sorted(find_lock_solutions(case_input)) == case_output

    @weight(0.8)
    @number('4.4')
    def test4(self):
        '''Test [2, 1, 0, 4, 5, 6, 7, 8, 9, 3]'''
        case_input = [2, 1, 0, 4, 5, 6, 7, 8, 9, 3]
        case_output = []
        assert sorted(find_lock_solutions(case_input)) == case_output

    @weight(0.8)
    @number('4.5')
    def test5(self):
        '''Secret Test'''
        case_input = [2, 3, 0, 6, "END", 5, 4, 8, 6, 8]
        case_output = ['1364', '7864', '9864']
        assert sorted(find_lock_solutions(case_input)) == case_output
