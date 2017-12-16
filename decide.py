#!/usr/bin/env python3

"""
Useful when I cannot decide something from a list of items.
"""

from collections import Counter
from random import randint
import time

counter = Counter()

candidates = []

for i in range(int(input('Number of items: '))):
    candidates.append(input('Candidate #{}: '.format(i + 1)))

minutes = float(input('Enter time in minutes: '))

start = time.time()

while True:
    counter.update(str(randint(1, len(candidates))))
    diff = (60 * minutes) - (time.time() - start)
    print("\rTime Remaining: {0:.5f}".format(diff if diff > 0  else 0), end='')
    if diff <= 0:
        # to add a new line
        print('\rTime Remaining: 0.' + '0' * 6)
        break

dashes = '------------'

print(dashes, 'Scores(asending order)', dashes)
print('\t'.join(['Index', 'Score', '%', 'Candidate']))

total_calls = sum(counter.values())

for i, index in enumerate(sorted(counter, key=lambda x: counter.get(x)), 1):
    candidate = candidates[int(index) - 1]
    score = counter.get(index)
    percentage = score / total_calls * 100

    print('\t'.join(map(lambda x: str(x),
                        [i, score, '{0:.5f}'.format(percentage), candidate])))
