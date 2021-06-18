#!/usr/bin/env python
# -*- coding: UTF8 -*-

import sys


class My_Brainfuck:
    """
    create object brainfuck
    """


def help_programme():
    """
    documentation to assist the user
    """
    print("USAGE")
    print("\t./my_brainfuckj.py programme.bf")
    print("DESCRIPTION")
    print("\tto be able to run programs written in brainfuck with the \".bf\" extension")
    sys.exit(0)

def buffer_file(filename):
    """
    vérify and parse the file programme
    """
    syntaxes_brainfuck = '-+><.,[] \n\t'
    split_name = filename.split(".bf")
    if split_name[len(split_name) - 1] not in ".bf":
        print("Error : The file is not a brainfuck program", file=sys.stderr)
        sys.exit(84)
    buffer = ""
    with open(filename, "r") as filin:
        for ligne in filin:
            for letter in ligne:
                if not letter in syntaxes_brainfuck:
                    print("Error : The character is not valid !", file=sys.stderr)
                    sys.exit(84)
            buffer += ligne
    return buffer

## PRINCIPALE PROGRAMME
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Error : too many or too few arguments. -h to watch the doc", file=sys.stderr)
        sys.exit(84)
    if (len(sys.argv) == 2 and sys.argv[1] in '-h'):
        help_programme()
    if (len(sys.argv) == 2):
        buffer_file(sys.argv[1])

