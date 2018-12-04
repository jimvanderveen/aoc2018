#!/usr/bin/env python

infile = 'drift.txt'

with open(infile, 'r') as f:
    drift_list = [int(x.strip()) for x in f.readlines()]
resulting_freq = sum(drift_list)
print('Resulting frequency:', resulting_freq)

# Now I need a dict to store the resulting freq, curr_freq.
# Report the first time a resulting freq is re-used.
curr_freq = 0
freqs = {}
freqs[curr_freq] = True
d_index = 0    # Index of the circular drift list.
first_repeated_freq = None
while first_repeated_freq is None:
    curr_freq += drift_list[d_index]
    if curr_freq not in freqs:
        freqs[curr_freq] = True
        d_index = (d_index + 1) % len(drift_list)
    else:
        first_repeated_freq = curr_freq    # loop exit condition
print('First freq to repeat:', first_repeated_freq)
