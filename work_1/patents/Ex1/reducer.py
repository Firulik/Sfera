#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
from itertools import groupby

splt = lambda line: line.strip().split('\t', 1)

for key, group in groupby((splt(line) for line in sys.stdin), lambda line: line[0]):
    print '%s\t%s' % (key,','.join([citing for cited, citing in group]))

    
