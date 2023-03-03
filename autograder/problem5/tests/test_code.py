import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number, visibility
from problem5 import largest_color


class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(0.8)
    @number('5.1')
    def test1(self):
        '''Test Sample 1'''

        case_input = [[1, 1, 2, 2, 2],
                      [3, 1, 1, 1, 2],
                      [3, 3, 1, 4, 4]
                      ]
        case_output = 6
        assert (largest_color(case_input)) == case_output

    @weight(0.8)
    @number('5.2')
    def test2(self):
        '''Test Sample 2'''
        case_input = [[1, 1, 2, 2, 2],
                      [3, 1, 1, 1, 2],
                      [3, 3, 1, 4, 2],
                      [3, 3, 4, 4, 2],
                      [1, 1, 1, 2, 2]
                      ]
        case_output = 8
        assert (largest_color(case_input)) == case_output

    @weight(0.8)
    @number('5.3')
    def test3(self):
        '''Test 6 rows, 5 cols (with each color occurring only once)'''
        case_input = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [6, 6, 3, 4, 5],
            [4, 4, 4, 4, 4]
        ]
        case_output = 10
        assert (largest_color(case_input)) == case_output

    @weight(0.8)
    @number('5.4')
    def test4(self):
        '''Test 4 rows, 6 cols'''
        case_input = [[5, 5, 5, 3, 3, 3],
                      [5, 3, 3, 5, 5, 5],
                      [5, 3, 2, 1, 1, 1],
                      [3, 5, 2, 2, 3, 3]]

        case_output = 5
        assert (largest_color(case_input)) == case_output

    @weight(0.8)
    @number('5.5')
    def test5(self):
        '''Secret Test'''
        case_input = [
            [3, 3, 3, 3, 3],
            [3, 1, 1, 1, 3],
            [3, 3, 3, 3, 3],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]

        ]
        case_output = 12
        assert (largest_color(case_input)) == case_output
