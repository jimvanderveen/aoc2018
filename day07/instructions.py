#!/usr/bin/env python

import pprint
import string

infile = 'tasks.list'
#infile = 'tasks.test'

task = {}

with open(infile, 'r') as f:
    for inst in f:
        words = inst.split()
        antecedent = words[1]
        successor = words[7]
        if successor in task:
            task[successor].add(antecedent)
        else:
            task[successor] = set(antecedent)

for t in sorted(task):
    print(t, pprint.pformat(task[t]))

all_tasks = set()
for t in task:
    all_tasks |= task[t]
print(pprint.pformat(all_tasks))

ordered_tasks = []
while all_tasks:
    available_tasks = []
    for t in all_tasks:
        if t not in task or len(task[t]) == 0:
            # Task T has no antecedents, it's available.
            available_tasks += t
            
    next_task = sorted(available_tasks)[0]
    print('Next task(s):', pprint.pformat(sorted(available_tasks)))
    ordered_tasks += next_task
    all_tasks.remove(next_task)
    ### print(pprint.pformat(all_tasks))
    # for t in all_tasks:
    for t in task:
        task[t] -= set(next_task)
        #if len(task[t]) == 0:
        #    del task[t]
#        if next_task in task[t]:
#            print('removing:', next_task, 'from:', t)
#            task[t].remove(next_task)
#        else:
#            print('task:', t, 'missing:', next_task)
    #for t in sorted(task):
    #    print(t, pprint.pformat(task[t]))

### print('There should be one remaining task:', pprint.pformat(task))
for t in task:
    if t not in ordered_tasks:
        print('Final task:', t)
        ordered_tasks += t
print(ordered_tasks)
