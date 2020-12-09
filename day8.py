#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 8
"""

import time

print('* DAY 8 *')

start = time.process_time()

with open('inputs/day8.txt') as inst_file:
    i = [x.split() for x in inst_file.read().splitlines()]
    
def run(instructions):
    pc = 0
    accumulator = 0
    seen = set()
    
    while pc < len(i):
        op, arg = i[pc]
    
        if pc in seen: break
        
        if op == 'acc': accumulator += int(arg)
        elif op == 'jmp': pc += int(arg) - 1
        elif op == 'nop': pass
    
        seen.add(pc)
        pc += 1
        
    return pc, accumulator

_, part1 = run(i)

swap_map = {'jmp': 'nop', 'nop': 'jmp'}
for c in range(len(i)):
    if i[c][0] != 'acc':
        i[c][0] = swap_map[i[c][0]]
        pc, accumulator = run(i)
        if pc == len(i):
            part2 = accumulator
            break
        i[c][0] = swap_map[i[c][0]]

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()