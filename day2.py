#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 2
"""

import time
import re

print('* DAY 2 *')

start = time.process_time()

with open('inputs/day2.txt') as passwords:
    entries = [re.split(r'[-\s:]+', x) for x in passwords.read().splitlines()]
    
part1, part2 = 0, 0
for e in entries:
    min_, max_ = int(e[0]), int(e[1])
    if min_ <= e[3].count(e[2]) <= max_: part1 += 1
    if (e[3][min_-1] == e[2]) != (e[3][max_-1] == e[2]): part2 += 1

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()