#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 18
"""

import time
import re

print('* DAY 18 *')

start = time.process_time() 

with open('inputs/day18.txt') as homework:
    problems = [re.split(r'(?<=\()|(?=\))|\s', x) for x in homework.read().splitlines()]

# Shunting-yard algorithm
def to_postfix(p, precedences):
    output, op_stack = [], []
    for c in p:
        if c.isnumeric(): output.append(int(c))
        elif c in {'+', '*'}:
            while op_stack and op_stack[-1] != '(' and precedences[op_stack[-1]] >= precedences[c]:
                output.append(op_stack.pop())
            op_stack.append(c)
        elif c == '(': op_stack.append(c)
        elif c == ')':
            while (p := op_stack.pop()) != '(':
                output.append(p)
    while op_stack: output.append(op_stack.pop())
    return output

def do_homework(problems, precedences):
    res = []
    for p in problems:
        postfix_form = to_postfix(p, precedences)
        for c in postfix_form:
            if c == '+': res.append(res.pop() + res.pop())
            elif c == '*': res.append(res.pop() * res.pop())
            else: res.append(c)
    return sum(res)

part1 = do_homework(problems, {'+':0, '*':0})
part2 = do_homework(problems, {'+':1, '*':0})

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()