#!/usr/bin/env python
import sys
import string

stop_words = ['a', 'an', 'and', 'are', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its',
              'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']

# translator punctuation to whitespace
# https://stackoverflow.com/questions/34860982/replace-the-punctuation-with-whitespace/34922745
translator = string.maketrans(string.punctuation, ' '*len(string.punctuation))

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace, convert to lowercase
    line = line.strip().lower()
    line - line.translate(translator)

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stop_words:
            print '%s\t%s' % (word, "1")
