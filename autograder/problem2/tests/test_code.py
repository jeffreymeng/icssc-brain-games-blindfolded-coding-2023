import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number, visibility
from problem2 import rewire_elevator

class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(0.8)
    @number('2.1')
    def test1(self):
        '''Test [-1, 1, 2, 3, 4, 5]'''

        case_input = [-1, 1, 2, 3, 4, 5]
        case_output = rewire_elevator(case_input)
        assert case_output is not None
        assert case_output[2] == -1, "The third element must take you to floor -1"
        assert sum(case_output) == sum(case_input), "The sum of the floors must not change"
        assert len(set(case_output)) == len(case_output), "There must not be any duplicate floors in your output"


    @weight(0.8)
    @number('2.2')
    def test2(self):
        '''Test [-1, 1, 2, 3]'''
        case_input = [-1, 1, 2, 3]
        case_output = rewire_elevator(case_input)
        assert case_output is not None
        assert case_output[2] == -1, "The third element must take you to floor -1"
        assert sum(case_output) == sum(case_input), "The sum of the floors must not change"
        assert len(set(case_output)) == len(case_output), "There must not be any duplicate floors in your output"

    @weight(0.8)
    @number('2.3')
    def test3(self):
        '''Test [-1, 1, 2, 3, 4, 5, 6, 7, 8]'''
        case_input = [-1, 1, 2, 3, 4, 5, 6, 7, 8]
        case_output = rewire_elevator(case_input)
        assert case_output is not None
        assert case_output[2] == -1, "The third element must take you to floor -1"
        assert sum(case_output) == sum(case_input), "The sum of the floors must not change"
        assert len(set(case_output)) == len(case_output), "There must not be any duplicate floors in your output"

    @weight(0.8)
    @number('2.4')
    def test4(self):
        '''Test [-1, 1, 2, 3] + list(range(4, 21))'''
        case_input = [-1, 1, 2, 3] + list(range(4, 21))
        case_output = rewire_elevator(case_input)
        assert case_output is not None
        assert case_output[2] == -1, "The third element must take you to floor -1"
        assert sum(case_output) == sum(case_input), "The sum of the floors must not change"
        assert len(set(case_output)) == len(case_output), "There must not be any duplicate floors in your output"

    @weight(0.8)
    @number('2.5')
    def test5(self):
        '''Secret Test'''
        case_input = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        case_output = rewire_elevator(case_input)
        assert case_output is not None
        assert case_output[2] == -1, "The third element must take you to floor -1"
        assert sum(case_output) == sum(case_input), "The sum of the floors must not change"
        assert len(set(case_output)) == len(case_output), "There must not be any duplicate floors in your output"

