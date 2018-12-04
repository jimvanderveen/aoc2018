#!/usr/bin/env python

infile = 'drift.txt'

drift_h = open(infile, 'r')
drift_list = drift_h.readlines()

total_drift = 0

# Now I need a dict to store the resulting freq, total_drift.
# Report the first time a resulting freq is re-used.
first_repeated_freq = None
freq = dict()
freq[total_drift] = 1    # This freq has appeared once.

for d in drift_list:
    total_drift += int(d)
    if total_drift in freq:
        # This frequency has appeared before, increment counter.
        freq[total_drift] += 1
        if first_repeated_freq is None:
            # First repeated frequency, report it!
            print('First freq to repeat:', first_repeated_freq)
    else:
        # New freq, note its appearance.
        ### print('    new freq:', total_drift)
        freq[total_drift] = 1
print('Total drift:', total_drift)
