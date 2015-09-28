#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
from itertools import groupby

for key, group in groupby(line.strip() for line in sys.stdin):
    print '%s\t%s' % (key,len([count for count in group]))

    
