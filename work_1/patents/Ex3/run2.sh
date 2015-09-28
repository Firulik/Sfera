#!/bin/sh
hadoop fs -rm -r aggregate

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -file mapper2.py \
    -mapper 'mapper2.py 1 4' \
    -reducer aggregate \
    -input /data/patents/apat63_99.txt \
    -output aggregate
