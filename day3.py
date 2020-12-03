#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 3
"""

import time

print('* DAY 3 *')

start = time.process_time()

with open('inputs/day3.txt') as area:
    trees = area.read().splitlines()
    
def numTrees(areaMap, slope):
    curr = (0,0) # column, row
    result = 0
    while curr[1] < len(areaMap):
        result += (areaMap[curr[1]][curr[0]] == '#')
        curr = ((curr[0] + slope[0]) % len(areaMap[0]), curr[1] + slope[1])
    return result

part1 = numTrees(trees, (3,1))
part2 = 1
for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    part2 *= numTrees(trees, slope)

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()