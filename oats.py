#!/bin/env python3
# *-* coding: utf-8 *-*

from dataclasses import dataclass
from typing import List
from sys import argv
import io

@dataclass
class Coord:
    x: int
    y: int

def in_bounds(coord: Coord, prog: List[str]) -> bool:
    return 0 <= coord.y < len(prog) and 0 <= coord.x < len(prog[coord.y])
def get_char(coord: Coord, prog: List[str]) -> str:
    return prog[coord.y][coord.x]

def execute(program):
    program = program.split('\n')
    pointer = Coord(0, 0)
    stack = []

    while in_bounds(pointer, program):
        char = get_char(pointer, program)
        if char == '⊤':
            # True.
            stack.append(True)
        elif char == '⊥':
            # False.
            stack.append(False)
        elif char in '0123456789':
            # Push number to the stack.
            num = []
            while char in '0123456789' and in_bounds(pointer, program):
                num.append(char)
                pointer.x += 1
                char = get_char(pointer, program)
            pointer.x -= 1
            stack.append(int(''.join(num)))
        elif char == '"':
            # Push text to the stack.
            string = []
            char = ''
            while char != '"' and in_bounds(pointer, program):
                if char == '\\':
                    pointer.x += 1
                    char = get_char(pointer, program)
                    if char == 'n':
                        string.append('\n')
                    else:
                        string.append(char)
                else:
                    string.append(char)
                pointer.x += 1
                char = get_char(pointer, program)
            stack.append(''.join(string))
        elif char == '⌃':
            # Pop from stack and print to stdout.
            print(stack.pop(), end='')
        elif char == '⌄':
            # Read from stdin and push to stack.
            stack.append(input())
        elif char == '⌥':
            # Duplicate top element of stack.
            val = stack.pop()
            stack.append(val)
            stack.append(val)
        elif char == '⌀':
            # Ditch the top element of the stack.
            stack.pop()
        elif char == '⤵':
            # Swap top two elements of the stack.
            x = stack.pop()
            y = stack.pop()
            stack.append(x)
            stack.append(y)
        elif char == '⍖':
            # Put top element of the stack at the bottom.
            stack = [stack[-1], *stack[:-1]]
        elif char == '⍏':
            # Put bottom element of the stack at the top.
            stack = [*stack[1:], stack[0]]
        elif char == '⍆':
            # Hop over next character.
            pointer.x += 1
        elif char == '⍋':
            # Pop string from stack, push first character, push rest of string.
            string = stack.pop()
            stack.append(string[0])
            stack.append(string[1:])
        elif char == '+':
            # Add.
            y, x = stack.pop(), stack.pop()
            stack.append(x + y)
        elif char == '·':
            # Multiply.
            y, x = stack.pop(), stack.pop()
            stack.append(x * y)
        elif char == '–':
            # Negate.
            stack.append(-stack.pop())
        elif char == '/':
            # Reciprocal.
            stack.append(1/stack.pop())
        elif char == '=':
            # Comparison operators.
            y, x = stack.pop(), stack.pop()
            stack.append(x == y)
        elif char == '≠':
            # Comparison operators.
            y, x = stack.pop(), stack.pop()
            stack.append(x != y)
        elif char == '<':
            # Comparison operators.
            y, x = stack.pop(), stack.pop()
            stack.append(x < y)
        elif char == '>':
            # Comparison operators.
            y, x = stack.pop(), stack.pop()
            stack.append(x > y)
        elif char == '≤':
            # Comparison operators.
            y, x = stack.pop(), stack.pop()
            stack.append(x <= y)
        elif char == '≥':
            # Comparison operators.
            y, x = stack.pop(), stack.pop()
            stack.append(x >= y)
        elif char == '¬':
            # NOT.
            stack.append(not stack.pop())
        elif char == '∧':
            # AND.
            y, x = stack.pop(), stack.pop()
            stack.append(x and y)
        elif char == '∨':
            # OR.
            y, x = stack.pop(), stack.pop()
            stack.append(x or y)
        elif char == '⎡':
            # Switch-case.
            for _ in range(stack.pop()):
                pointer.y += 1
                if not in_bounds(pointer, program):
                    break
                char = get_char(pointer, program)
                if char == '⎣':
                    break
        elif char in '⎢⎣':
            # Oops! We rammed into part of a switch case.
            nestedness = 1
            while nestedness>0 and in_bounds(pointer, program):
                pointer.x += 1
                char = get_char(pointer, program)
                if char in '⎢⎣':
                    nestedness += 1
                elif char in '⎥⎦⎬⎭':
                    nestedness -= 1
        elif char in '⎤⎥⎦':
            # Switch case end.
            while char != '⎤' and in_bounds(pointer, program):
                pointer.y -= 1
                char = get_char(pointer, program)
        elif char in '⎫⎬⎭}':
            # Loop.
            nestedness = 1
            while nestedness>0 and in_bounds(pointer, program):
                pointer.x -= 1
                char = get_char(pointer, program)
                if char in '⎡⎢⎣[':
                    nestedness -= 1
                elif char in '⎤⎥⎦⎫⎬⎭]':
                    nestedness += 1
        elif char == 'ℝ':
            # Cast to float.
            stack.append(float(stack.pop()))
        elif char == 'ℤ':
            # Cast to int.
            stack.append(int(stack.pop()))
        elif char == 'ℙ':
            # Cast to string.
            stack.append(str(stack.pop()))
        pointer.x += 1
    print('\n\n--- PROGRAM FINISHED ---')
    print('STACK DUMP:', stack)

if __name__ == '__main__':
    if len(argv)==1:
        print('usage: oats.py [filename]')
        exit()
    with io.open(' '.join(argv[1:]), 'r', encoding='utf-8') as file:
        execute(file.read())
