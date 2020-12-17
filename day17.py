#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 17
"""

import time
import numpy as np
from scipy.ndimage import convolve

print('* DAY 17 *')

start = time.process_time() 

with open('inputs/day17.txt') as file:
    grid = np.array([[[int(c == '#') for c in r] for r in file.read().splitlines()]])

def conway_cubes(grid, iters):
    curr_grid = np.pad(grid, 1)
    kernel = np.ones(tuple([3] * grid.ndim))
    kernel[tuple([1] * grid.ndim)] = 0
    for _ in range(iters):
        res = convolve(curr_grid, kernel, mode='constant')
        curr_grid = np.pad(np.where((res == 3) | (curr_grid & (res == 2)), 1, 0), 1)
    return curr_grid
    
part1 = np.sum(conway_cubes(grid, 6))
part2 = np.sum(conway_cubes(grid[..., None], 6))

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()