#!/bin/sh
hadoop fs -rm -r counts

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	 -file mapper.py reducer.py \
	 -mapper mapper.py \
	 -reducer reducer.py \
	 -input patents/part* \
	 -output counts

