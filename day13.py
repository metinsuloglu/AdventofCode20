#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 13
"""

import time
from sympy.ntheory.modular import crt

print('* DAY 13 *')

start = time.process_time()

with open('inputs/day13.txt') as notes:
    earliest_time, busses = notes.read().splitlines()
    earliest_time, busses = int(earliest_time), [int(x) if x != 'x' else -1 for x in busses.split(',')]

min_wait = float('inf')
for b in busses:
    if b == -1: continue
    wait_time = b - (earliest_time % b)
    if wait_time < min_wait:
        min_wait = wait_time
        part1 = b * wait_time
        
moduli = [b for b in busses if b != -1]
residues = [b - i for i,b in enumerate(busses) if b != -1]
part2 = int(crt(moduli, residues, check=False)[0])

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()