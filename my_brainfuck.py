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

class Node:
    """
    Linked List in python
    """
    def __init__(self, value):
        """
        construct list
        """
        self.value = value
        self.next = None

class Stack:
    """
    Create object Stack
    """
    def __init__(self):
        """
        init the stack
        """
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        """
        String represente the Stack when we print
        """
        current = self.head.next
        recup_value = ""
        while current:
            recup_value += str(current.value) + '->'
            current = current.next
        return recup_value[:-2]

    def getSize(self):
        """
        Get the current size of the stack
        """
        return self.size

    def isEmpty(self):
        """
        Check if the stack is empty
        """
        return self.size == 0

    def push(self, value):
        """
        Push the value into the stack
        """
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        """
        Remove the value from the stack and return
        """
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

class My_Brainfuck:
    """
    create object brainfuck
    """
    def __init__(self):
        """
        construct the the object
        """
        self.pc = 0
        self.ptr = 0
        self.stack_loop = Stack()
        self.code_progr = []
        self.mem = [0] * 90000
        self.actions = {
            '<' : (self._opp_ptr,(-1)),
            '>' : (self._opp_ptr,(1)),
            '+' : (self._incr_val,(1)),
            '-' : (self._incr_val,(-1)),
            '.' : (self._put_char,(0)),
            ',' : (self._get_char,(0)),
            '[' : (self._enter_loop,(0)),
            ']' : (self._exit_loop,(0))
        }

    def _enter_loop(self, nothing):
        """
        enter in the loop
        """
        self.stack_loop.push(self.pc)

    def _jmp(self):
        """
        jmp to this instruction
        """
        label = self.stack_loop.pop()
        self.pc = label - 1 # intruction avant comme sa il fait + 1 pour ceux retourver à l'instruction '['

    def _exit_loop(self, nothing):
        """
        exit in the loop
        """
        if self.mem[self.ptr] == 0:
            self.stack_loop.pop()
        else:
            self._jmp()

    def parse_string(self, string):
        """
        parse the string programme
        """
        for i in range(len(string)):
            self.code_progr.append(string[i])

    def _opp_ptr(self, i):
        """
        pointer operation
        """
        self.ptr += i

    def _incr_val(self, i):
        """
        increment the value where is the pointer
        """
        self.mem[self.ptr] += i

    def _put_char(self, nothing):
        """
        print the ASCII character
        """
        print(chr(self.mem[self.ptr]), sep='', end='')

    def _get_char(self, nothing):
        """
        entry of a byte in the array where the pointer is positioned (ASCII value).
        """
        self.mem[self.ptr] = ord(sys.stdin.read(1))

    def execute_progr(self):
        """
        run program code
        """
        while self.pc < len(self.code_progr):
            instruction = self.code_progr[self.pc]
            action, argv = self.actions[instruction] # passer un dictionnaire en arguments de functions
            action(argv)
            self.pc += 1

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
        bf = My_Brainfuck()
        bf.parse_string(buffer)
        bf.execute_progr()
