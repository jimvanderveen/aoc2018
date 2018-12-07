#!/usr/bin/env python

from pprint import pprint

infile = 'labels.dat'

# Read all the boxes' labels.
# For each box label, count the number of each character.
# Build a dict indexed by character, store the counts.
# Use has_pair/triple to compute the "checksum" for part 1.

class Box_Label:
    def __init__(self, label):
        # Assume no pairs/triples, set these after counting letters.
        self.has_pair = False
        self.has_triple = False
        self.box_label = label
        self.length = len(label)
        self.letter_counts = {}
        for c in label:
            if c in self.letter_counts:
                self.letter_counts[c] += 1
            else:
                self.letter_counts[c] = 1
        for c in self.letter_counts:
            self.has_pair = self.has_pair or ( 2 == self.letter_counts[c] )
            self.has_triple = self.has_triple or ( 3 == self.letter_counts[c] )

labels = []      # The list of box labels and derived info
pairs = 0        # Number of labels with at least 1 pair of letters
triples = 0      # Number of labels with at least 1 triple of letters
label_len = 0    # Length of all labels (so far)
with open(infile, 'r') as f:
    for label_text in f:
        this_label = Box_Label( label_text )
        # Initialize with length of first label, then ensure the rest are same size.
        if label_len == 0:
            label_len = this_label.length
        else:
            if this_label.length != label_len:
                print('Label length mismatch! Expected:', label_len, 'but got:', this_label.length, this_label.box_label)
        # pprint(vars(this_label))
        pairs += this_label.has_pair
        triples += this_label.has_triple
        labels.append( this_label )    # Save in case needed for part 2

print('Length of all labels:', label_len)
print('Number of boxes:', len(labels))
print('Checksum:', pairs*triples)

# Now I need to find box labels which match in all but 1 position.
# Almost-matching boxes will have to match on 1..x OR 2..end
