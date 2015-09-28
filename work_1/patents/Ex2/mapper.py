#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    cited, value = line.strip().split('\t',1)
    print len(value.split(','))
