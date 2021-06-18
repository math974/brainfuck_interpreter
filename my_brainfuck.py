#!/usr/bin/env python
# -*- coding: UTF8 -*-

import sys
import re

"""
Date : 18/06/2021
Auteur : Mathias BALLOT
Project : brainfuck interpreter
Licence : MIT
"""

class My_Brainfuck:
    """
    create object brainfuck
    """
    def __init__(self):
        """
        construct the the object
        """
        self.i_code = 0
        self.ptr = 0
        self.mem = [0] * 90000
        self.actions = {
            '<' : (None, self.opp_ptr(-1)),
            '>' : (None, self.opp_ptr(1)),
            '+' : (None, self.incr_val(1)),
            '-' : (None, self.incr_val(-1))
        }

    def opp_ptr(self, i):
        """
        pointer operation
        """
        self.ptr += i

    def incr_val(self, i):
        """
        increment the value where is the pointer
        """
        self.mem[self.ptr] += i

    def execute_progr(self):
        """
        run program code
        """


def help_programme():
    """
    documentation to assist the user
    """
    print("USAGE")
    print("\t./my_brainfuck.py programme.bf")
    print("DESCRIPTION")
    print("\tTo be able to run programs written in brainfuck with the \".bf\" extension")
    print("\tThe interpreter also handles comments")
    print("\tcharacter accept : \"><.,[]\\t\\n#\" + space")
    sys.exit(0)

def buffer_file(filename):
    """
    vérify and parse the file programme
    """
    split_name = filename.split(".bf")
    if split_name[len(split_name) - 1] not in ".bf":
        print("Error : The file is not a brainfuck program", file=sys.stderr)
        sys.exit(84)
    buffer = ""
    try:
        with open(filename, "r") as filin:
            for ligne in filin:
                buffer += ligne
    except FileNotFoundError as e:
        print("Error : File does not exist !", file=sys.stderr)
        sys.exit(84)
    except IOError as e:
        print("Error : file does not exist !", file=sys.stderr)
        sys.exit(84)
    return buffer

def delate_comment(buffer):
    """
    delete comments from the program
    """
    new_buffer = re.sub(r"#[^\n]*", "", buffer)
    return (new_buffer)

def check_invalid_character(buffer):
    """
    check the invalid charact
    """
    syntaxes_brainfuck = '-+><.,[] \n\t'
    for letter in buffer:
        if not letter in syntaxes_brainfuck:
            print("Error : The character is not valid !", file=sys.stderr)
            sys.exit(84)

## PRINCIPALE PROGRAMME
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Error : too many or too few arguments. -h to watch the doc", file=sys.stderr)
        sys.exit(84)
    if (len(sys.argv) == 2 and sys.argv[1] in '-h'):
        help_programme()
    if (len(sys.argv) == 2):
        buffer = buffer_file(sys.argv[1])
        buffer = delate_comment(buffer)
        check_invalid_character(buffer)
        buffer = re.sub(r"[\s]+", "", buffer) # remove white characters
        print(buffer)

