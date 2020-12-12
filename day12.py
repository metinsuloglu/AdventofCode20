#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 12
"""

import time

print('* DAY 12 *')

start = time.process_time()

with open('inputs/day12.txt') as file:
    instructions = [(x[0], int(x[1:])) for x in file.read().splitlines()]

def move(direction, amount, pos):
    if direction == 'N': pos = (pos[0], pos[1] - amount)
    elif direction == 'S': pos = (pos[0], pos[1] + amount)
    elif direction == 'E': pos = (pos[0] + amount, pos[1])
    elif direction == 'W': pos = (pos[0] - amount, pos[1])
    return pos
    
def rotate(direction, amount, relative_coord):
    for r in range(amount // 90):
        if direction == 'R': relative_coord = (-relative_coord[1], relative_coord[0])
        else: relative_coord = (relative_coord[1], -relative_coord[0])
    return relative_coord

def run(command, amount, curr_pos, waypoint_pos):
    if command in {'R','L'}:
        waypoint_pos = rotate(command, amount, waypoint_pos)
    elif command  == 'F':
        curr_pos = (curr_pos[0] + amount * waypoint_pos[0], curr_pos[1] + amount * waypoint_pos[1])
    elif command in {'N','S','E','W'}:
        curr_pos = move(command, amount, curr_pos)
    return curr_pos, waypoint_pos

loc = (0,0)
wp_pos = (1,0)
for i, n in instructions: loc, wp_pos = run(i, n, loc, wp_pos)
    
part1 = sum(abs(x) for x in loc)

loc = (0,0)
wp_pos = (10,-1)
for i, n in instructions:
    if i in {'N','E','S','W'}: wp_pos = move(i, n, wp_pos)
    else: loc, wp_pos = run(i, n, loc, wp_pos)

part2 = sum(abs(x) for x in loc)

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()