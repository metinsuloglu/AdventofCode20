#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 14
"""

import time
import re
from collections import defaultdict

print('* DAY 14 *')

start = time.process_time()

with open('inputs/day14.txt') as file:
    instructions = [re.findall(r'\w+', x) for x in file.read().splitlines()]
    
def apply_mask(n, mask):
    b_n = list(bin(n)[2:].zfill(36))
    for bit in range(len(mask)):
        if mask[bit] != 'X': b_n[bit] = mask[bit]
    return int(''.join(b_n), 2)

mem = defaultdict(int)
for i in instructions:
    if i[0] == 'mask': curr_mask = i[1]
    else: mem[i[1]] = apply_mask(int(i[2]), curr_mask)

part1 = sum(mem.values())

def all_masks(mask):
    if mask == '': yield ''
    else:
        for m in all_masks(mask[1:]):
            if mask[0] == '0': yield 'X' + m
            elif mask[0] == '1': yield '1' + m
            elif mask[0] == 'X': yield '0' + m; yield '1' + m

mem.clear()
for i in instructions:
    if i[0] == 'mask': curr_mask = i[1]
    else:
        for m in all_masks(curr_mask):
            mem[apply_mask(int(i[1]), m)] = int(i[2])
            
part2 = sum(mem.values())
    
end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()