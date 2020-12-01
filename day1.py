#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 1
"""

import time

print('* DAY 1 *')

start = time.process_time()

with open('inputs/day1.txt') as report:
    entries = [int(x) for x in report.read().splitlines()]

def findSum(entries, total):
    d = set()
    for e in entries:
        if e in d:
            return e, (total - e)
        else: d.add(total - e)
    return None
    
res = findSum(entries, 2020)
part1 = res[0] * res[1]

for i, e in enumerate(entries):
    res = findSum(entries[i+1:], 2020 - e)
    if res:
        part2 = res[0] * res[1] * e
        break

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()