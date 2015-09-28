#!/bin/sh
hadoop fs -rm -r patents

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	 -file mapper.py reducer.py \
	 -mapper mapper.py \
	 -reducer reducer.py \
	 -input /data/patents/cite75_99.txt \
	 -output patents

