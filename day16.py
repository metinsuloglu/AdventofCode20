#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 16
"""

import time
import re
from collections import defaultdict

print('* DAY 16 *')

start = time.process_time()

with open('inputs/day16.txt') as file:
    info = file.read().split('\n\n')
    field_rules = [re.split(r': | or ', x) for x in info[0].split('\n')]
    field_rules = {r[0]: [tuple(map(int, re.fullmatch(r'(\d+)-(\d+)', n).groups()))
                          for n in r[1:]] for r in field_rules}
    my_ticket = [int(i) for i in info[1].split('\n')[1].split(',')]
    nearby_tickets = [[int(i) for i in row.split(',')] for row in info[2].split('\n')[1:]]
    
def is_valid(n, range_list):
    for r in ranges:
        if r[0] <= k <= r[1]: return True
    return False

field_poss = defaultdict(lambda: set(range(len(my_ticket))))
part1 = 0
for ticket in nearby_tickets:
    for idx, k in enumerate(ticket):
        v = False
        invalid_fields = []
        for field_id, ranges in field_rules.items():
            if is_valid(k, ranges): v = True
            else: invalid_fields.append(field_id)
        if not v: part1 += k
        else: 
            for ivf in invalid_fields: field_poss[ivf] -= {idx}
            
assigned = {}
while len(assigned) != len(field_rules):
    for f in field_rules:
        field_poss[f] -= set(assigned.values())
        poss = field_poss[f]
        if len(poss) == 1: assigned[f] = poss.pop()
            
part2 = 1
for k, v in assigned.items():
    if k.startswith('departure'): part2 *= my_ticket[v]

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()