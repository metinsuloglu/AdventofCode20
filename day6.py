#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 6
"""

import time

print('* DAY 6 *')

start = time.process_time()

with open('inputs/day6.txt') as file:
    answers = [[set(x) for x in a.splitlines()] for a in file.read().split('\n\n')]

part1 = sum([len(s) for s in [set.union(*x) for x in answers]])
part2 = sum([len(s) for s in [set.intersection(*x) for x in answers]])
    
end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()