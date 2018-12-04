#!/usr/bin/env python

infile = 'drift.txt'

drift_h = open(infile, 'r')
drift_list = drift_h.readlines()
total_drift = 0
for d in drift_list:
    total_drift += int(d)
print('Total drift:', total_drift)
