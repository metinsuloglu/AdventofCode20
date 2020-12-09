#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 7
"""

import time
import re
from collections import defaultdict

print('* DAY 7 *')

start = time.process_time()

with open('inputs/day7.txt') as rule_file:
    rules = [r.split(' bags contain ') for r in rule_file.read().splitlines()]

contains, contained_in = defaultdict(list), defaultdict(list)
for r in rules:
    contains[r[0]] = re.findall(r'(\d+) ([\w ]+) bag[s, ]*', r[1])
    for bag in contains[r[0]]: contained_in[bag[1]].append(r[0])
    
seen = set()
q = ['shiny gold']
while q:
    curr_bag = q.pop()
    for b in contained_in[curr_bag]:
        if b not in seen:
            q.append(b)
            seen.add(b)
        
part1 = len(seen)

def count_contained_bags(bag):
    n_bags = 0
    for n, b in contains[bag]:
        n_bags += int(n) * (count_contained_bags(b) + 1)
    return n_bags
    
part2 = count_contained_bags('shiny gold')

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()