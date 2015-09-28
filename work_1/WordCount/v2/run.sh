#!/bin/sh
hadoop fs -rm -r test

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	 -file mapper.py reducer.py \
	 -mapper mapper.py \
	 -reducer reducer.py \
	 -input /data/books/*.txt \
	 -output test

