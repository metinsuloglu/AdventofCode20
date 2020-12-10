#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 10
"""

import time

print('* DAY 10 *')

start = time.process_time()

with open('inputs/day10.txt') as file:
    jolts = [0] + [int(n) for n in file.read().splitlines()]
    jolts.append(max(jolts) + 3)
    jolts.sort()
    
diffs = [jolts[i + 1] - jolts[i] for i in range(len(jolts) - 1)]
n_ones = diffs.count(1)

part1 = n_ones * (len(diffs) - n_ones)

dp = [1] + [0] * (len(jolts) - 1)
for i in range(1, len(jolts)):
    j = i - 1
    while j >= 0 and jolts[i] - jolts[j] <= 3:
        dp[i] += dp[j]
        j -= 1
        
part2 = dp[-1]
    
end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()