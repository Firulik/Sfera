#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, re
from itertools import groupby

def read_input(file):
    splitter = re.compile('\W*')
    for line in file:
        yield [(word, len([v for v in values])) for word, values in groupby(sorted([word for word in splitter.split(line) if word != '']))]
 
def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word, count in words:
            print '%s%s%d' % (word, separator, count)

if __name__ == "__main__":
    main()
