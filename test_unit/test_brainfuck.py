
from my_brainfuck import My_Brainfuck
import unittest
import io
import sys

class Test_brainfuck_object(unittest.TestCase):
    """
    Test case used to test the functions of the 'brainfuck' module
    """

    def test_brainfuck_parse(self):
        """
        Test the operation of the 'parse_string' functions
        """
        bf = My_Brainfuck()
        bf.parse_string("..>>,,<<..")
        array_parse = ['.', '.', '>', '>', ',', ',', '<', '<', '.', '.']
        self.assertEqual(bf.code_progr, array_parse)