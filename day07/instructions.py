#!/usr/bin/env python

from pprint import pprint
from pprint import pformat
import string
import sys

debug = False

infile = 'tasks.list'
#infile = 'tasks.test'

class Worker:
    # is_idle (boolean function)
    # current task (or None, if idle)
    # [SORT KEY] finish_time (or sys.maxsize, if idle)
    # name (mostly for debugging, and fun)
    def __init__(self, name):
        self.name = name
        self.task = None
        self.finish_time = sys.maxsize

    def __lt__(self, other):
        return self.finish_time < other.finish_time

    def is_idle(self):
        return self.task is None

    def __repr__(self):
        # repr seems to be used for pprint()?
        if self.task is None:
            return "%s idle" % self.name
        else:
            return "%s on %s done %d" % (self.name, self.task, self.finish_time)

    def __str__(self):
        # str seems to be used for print()?
        return "%s(%r)" % (self.__class__, self.__dict__)

    def start(self, task, now):
        # Assign task to this worker.
        # Pass in the task label and the current time.
        # Return this worker's finish time.
        self.task = task
        self.finish_time = now + 61 + ord(task) - ord('A')
        return self.finish_time

    def finished(self):
        # Set this worker to idle.
        self.task = None
        self.finish_time = sys.maxsize

# Record all tasks' antecedents. Key: successor; value: set of antecedents.
antecedents = {}

all_tasks = set()

with open(infile, 'r') as f:
    for inst in f:
        words = inst.split()
        antecedent = words[1]
        successor = words[7]
        # Add both antecedent and successor to set of all_tasks
        all_tasks |= set(antecedent)
        all_tasks |= set(successor)
        # Record the dependency by adding to or creating the set of antecedents
        if successor in antecedents:
            antecedents[successor].add(antecedent)
        else:
            antecedents[successor] = set(antecedent)
if debug:
    #pprint(all_tasks)
    print(sorted(all_tasks))
    print('Number of tasks:',len(all_tasks))
if True:
    print('Tasks with antecedents')
    for t in sorted(antecedents):
        print(t, pformat(antecedents[t]))

workers = [Worker('elf1'), Worker('elf2'), Worker('elf3'), Worker('elf4'), Worker('I/me')]

current_time = 0

# We'll use min() to find next_event, so start with a number larger than any
# we're likely to see.
next_event = sys.maxsize

ordered_tasks = []
while all_tasks:
    # Which tasks are available now?
    available_tasks = []
    for t in sorted(all_tasks):
        if t not in antecedents or len(antecedents[t]) == 0:
            # Task T has no antecedents, it's available.
            available_tasks += t
    if debug:
        print('Next task(s):', pformat(available_tasks))

    # Which workers are idle?
    idle_workers = [w for w in workers if w.is_idle()]
    if debug:
        print('Idle worker(s):', idle_workers)

    # Assign available tasks to idle workers.
    while available_tasks and idle_workers:
        w = idle_workers.pop(0)
        t = available_tasks.pop(0)
        ordered_tasks += t
        if debug:
            pprint(ordered_tasks)
        f = w.start(t, current_time)
        all_tasks.remove(t)
        if debug:
            print(w)
            print('finish time:', f)

    # When will the next thing happen? Advance the clock to the earliest task
    # completion time, and figure out what's been done.
    if True:
    #if debug:
        print('Workers\' status:',workers)
    # Idle workers have ~infinite finish_time. I think it's possible for
    # multiple tasks to complete at the same time.
    next_worker = min(workers)
    if True:
    #if debug:
        print('Next event:', next_worker)
    if debug:
        pprint(all_tasks)

    for t in antecedents:
        antecedents[t] -= set(next_worker.task)
    if debug:
        for t in sorted(antecedents):
            print(t, pformat(antecedents[t]))

    print('Worker:',next_worker.name,'finished:', next_worker.task)
    current_time = next_worker.finish_time
    next_worker.finished()
    print('Workers\' status:',workers)
    if True:
        print('Time:',current_time)

print(ordered_tasks)
