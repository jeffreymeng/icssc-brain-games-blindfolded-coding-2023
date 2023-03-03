import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number
import subprocess

class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(0.5)
    @number('1.1')
    @tags('integration')
    def test1(self):
        '''Line 1'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')

        self.assertTrue(len(stdout) >= 1)
        self.assertEqual(stdout[0], 'l3tz dooo this')
        hello.terminate()

    @weight(0.5)
    @number('1.2')
    @tags("integration")
    def test2(self):
        '''Line 2'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 2)
        self.assertEqual(stdout[1], str(23 ** 5))
        hello.terminate()

    @weight(0.5)
    @number('1.3')
    @tags("integration")
    def test3(self):
        '''Line 3'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 3)
        self.assertEqual(stdout[2], "there they're their it's ok")
        hello.terminate()

    @weight(0.5)
    @number('1.4')
    @tags("integration")
    def test4(self):
        '''Line 4'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 4)
        self.assertEqual(stdout[3], "\"")
        hello.terminate()

    @weight(0.5)
    @number('1.5')
    @tags("integration")
    def test5(self):
        '''Line 5'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 5)
        self.assertEqual(stdout[4], 'a double quote')
        hello.terminate()

    @weight(0.5)
    @number('1.6')
    @tags("integration")
    def test6(self):
        '''Line 6'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 6)
        self.assertTrue(stdout[5] == 'bob then the words a quote then an actual quote')
        hello.terminate()

    @weight(0.5)
    @number('1.7')
    @tags("integration")
    def test7(self):
        '''Line 7'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 7)
        self.assertEqual(stdout[6], 'hi wait you typed it wrong go back two characters ok this time you really did type it wrong press delete stop')
        hello.terminate()

    @weight(0.5)
    @number('1.8')
    @tags("integration")
    def test8(self):
        '''Line 8'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 8)
        self.assertEqual(stdout[7], str(max(248 ** 30, 4 ** 200, 45 ** 45)))
        hello.terminate()
