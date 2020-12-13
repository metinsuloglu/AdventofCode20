#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 11
"""

import time
import numpy as np
from scipy.ndimage import convolve

print('* DAY 11 *')

start = time.process_time()

grid_converter = str.maketrans('.L#','012')
with open('inputs/day11.txt') as layout:
    grid = np.array([[int(x) for x in list(r.translate(grid_converter))]
                     for r in layout.read().splitlines()])


kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
curr_seats = np.copy(grid)
while True:
    prev_seats = np.copy(curr_seats)
    res = convolve(np.where(curr_seats == 2, 1, 0), kernel, mode='constant')
    curr_seats[(curr_seats == 1) & (res == 0)] = 2
    curr_seats[(curr_seats == 2) & (res >= 4)] = 1
    if (prev_seats == curr_seats).all(): break
                
part1 = np.count_nonzero(curr_seats == 2)


kernel = np.zeros((3,3,8))
kernel[(0,0,0,1,1,2,2,2), (0,1,2,0,2,0,1,2), range(8)] = 1.
curr_seats = np.copy(grid)
dp = np.zeros((curr_seats.shape[0] + 2, curr_seats.shape[1] + 2, 8))
while True:
    prev_seats = np.copy(curr_seats)
    dp[1:-1, 1:-1, :] = curr_seats[..., None]
    floor = np.where(curr_seats == 0)
    
    # forwards
    for i,j in zip(*floor):
        for idx, offset in enumerate([(-1,-1), (-1,0), (-1,1), (0,-1)]):
            dp[i+1, j+1, idx] = dp[i+1 + offset[0], j+1 + offset[1], idx]
    
    # backwards
    for i,j in zip(*[reversed(x) for x in floor]):
        for idx, offset in enumerate([(0,1), (1,-1), (1,0), (1,1)]):
            dp[i+1, j+1, idx+4] = dp[i+1 + offset[0], j+1 + offset[1], idx+4]
            
    res = convolve(np.where(dp[1:-1, 1:-1, :] == 2, 1, 0), kernel, mode='constant')[..., 3]
    curr_seats[(curr_seats == 1) & (res == 0)] = 2
    curr_seats[(curr_seats == 2) & (res >= 5)] = 1
    if (prev_seats == curr_seats).all(): break

part2 = np.count_nonzero(curr_seats == 2)


end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()
