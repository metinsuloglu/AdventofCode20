#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 9
"""

import time

print('* DAY 9 *')

start = time.process_time()

with open('inputs/day9.txt') as file:
    numbers = [int(n) for n in file.read().splitlines()]
    
def containsSum(n_list, total):
    m = set()
    for n in n_list:
        if n in m and (total - n) != m: return True
        m.add(total - n)
    return False 

preamble_size = 25
for i in range(preamble_size, len(numbers)):
    if not containsSum(numbers[i-preamble_size:i], numbers[i]):
        part1 = numbers[i]
        break

p1, p2 = 0, 1
curr_sum = numbers[p1] + numbers[p2]
while p2 < len(numbers):
    if curr_sum == part1: break
    elif curr_sum < part1:
        p2 += 1
        curr_sum += numbers[p2]
    elif curr_sum > part1:
        curr_sum -= numbers[p1]
        p1 += 1

contiguous_set = numbers[p1:p2+1]
part2 = min(contiguous_set) + max(contiguous_set)
    
end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()