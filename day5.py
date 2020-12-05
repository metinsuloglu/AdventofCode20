#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 5
"""

import time

print('* DAY 5 *')

start = time.process_time()

binary_converter = str.maketrans('FBLR','0101')
with open('inputs/day5.txt') as file:
    boarding_passes = [b.translate(binary_converter) for b in file.read().splitlines()]

seatIDs = sorted([int(b, 2) for b in boarding_passes])

part1 = seatIDs[-1]
part2 = (seatIDs[-1] * (seatIDs[-1] + 1) - (seatIDs[0] - 1) * seatIDs[0]) // 2 - sum(seatIDs)
    
end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()