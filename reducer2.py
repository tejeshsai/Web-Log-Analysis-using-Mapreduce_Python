#!/usr/bin/python

import sys
import collections

counter = collections.Counter()

for line in sys.stdin:
    k, v = line.strip().split("\t", 2)

    counter[k] += int(v)

print counter.most_common(
3)
