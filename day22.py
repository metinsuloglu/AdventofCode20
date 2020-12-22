#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
adventofcode.com

Day 22
"""

import time
from collections import deque
from itertools import islice
import copy

print('* DAY 22 *')

start = time.process_time()

with open('inputs/day22.txt') as cards:
    decks = [deque(int(x) for x in s.splitlines()[1:]) for s in cards.read().split('\n\n')]
    num_cards = sum(len(d) for d in decks)
            
def get_score(deck):
    return sum((i + 1) * deck.pop() for i in range(len(deck)))

def play_combat(decks, num_cards):
    while True:
        top_cards = [c.popleft() for c in decks]
        decks[max(enumerate(top_cards), key=lambda x:x[1])[0]].extend(sorted(top_cards, reverse=True))
        for i in range(len(decks)):
            if len(decks[i]) == num_cards: return decks[i]

part1 = get_score(play_combat(copy.deepcopy(decks), num_cards))

def play_recursive_combat(decks, num_cards):
    seen = set()
    while True:
        curr_config = tuple(decks[0] + deque(['']) + decks[1])
        if curr_config in seen: return 0
        else: seen.add(curr_config)
        
        top_cards = [c.popleft() for c in decks]
        if top_cards[0] <= len(decks[0]) and top_cards[1] <= len(decks[1]):
            winner = play_recursive_combat([deque(islice(decks[i], top_cards[i])) for i in range(len(decks))], sum(top_cards))
        else:
            winner = max(enumerate(top_cards), key=lambda x:x[1])[0]
        
        decks[winner].extend([top_cards[winner], top_cards[1 - winner]]) 
        for i in range(len(decks)):
            if len(decks[i]) == num_cards: return i
    
part2 = get_score(decks[play_recursive_combat(decks, num_cards)])

end = time.process_time()

print('PART 1:', part1)
print('PART 2:', part2)

print('Time:', round((end - start) * 1000, 3), 'ms')
print()