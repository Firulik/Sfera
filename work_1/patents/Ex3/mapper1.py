#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

index = int(sys.argv[1])
for line in sys.stdin:
    if line.startswith('"'): continue
    fields = line.split(',')
    print "LongValueSum:%s\t1" % fields[index]
