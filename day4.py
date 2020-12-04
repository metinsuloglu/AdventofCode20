#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 4
"""

import time
import re
import pandas as pd

print('* DAY 4 *')

start = time.process_time()

with open('inputs/day4.txt') as data:
    passports = pd.DataFrame([dict(re.findall(r'(\S+):(\S+)\s*', p)) \
                     for p in data.read().split('\n\n')], dtype=float)
    
def return_valid(passports, check_fields=False):
    valid = passports.dropna(subset=['byr','iyr','eyr','hgt','hcl','ecl','pid'])
    if check_fields:
        valid = valid[(valid['byr'].between(1920, 2002)) &
                      (valid['iyr'].between(2010, 2020)) &
                      (valid['eyr'].between(2020, 2030)) &
                      (valid['hgt'].apply(lambda x: \
                                          (x.endswith('cm') and (150 <= int(x[:-2]) <= 193)) \
                                          or (x.endswith('in') and (59 <= int(x[:-2]) <= 76)))) &
                      (valid['hcl'].str.fullmatch(r'#[0-9a-f]{6}')) &
                      (valid['ecl'].isin(['amb','blu','brn','gry','grn','hzl','oth'])) &
                      (valid['pid'].str.len() == 9)]
    return valid
    
part1 = len(return_valid(passports))
part2 = len(return_valid(passports, check_fields=True))

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()