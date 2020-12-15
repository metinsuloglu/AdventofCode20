#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 15
"""

import time

print('* DAY 15 *')

start = time.process_time()

starting_numbers = [0,5,4,1,10,14,7]

def get_nth(starting_numbers, n):
    seen = {n: i for i, n in enumerate(starting_numbers[:-1])}
    last_num = starting_numbers[-1]
    
    for i in range(len(starting_numbers), n):
        if last_num in seen:
            last_seen = seen[last_num]
            seen[last_num] = i - 1
            last_num = i - 1 - last_seen
        else:
            seen[last_num] = i - 1
            last_num = 0
    return last_num

part1 = get_nth(starting_numbers, 2020)
part2 = get_nth(starting_numbers, 30000000)
    
end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()