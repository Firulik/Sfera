#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from itertools import groupby
from operator import itemgetter
import sys
 
# читаем выход мэппера
# и разбиваем каждую пару на ключ-значение
# по знаку табуляции
def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)
 
def main(separator='\t'):
    # будем читать из стандартного потока ввода
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["<current_word>", "<count>"] items
    # с помощью  groupby группирует пары "слово-число вхождений" 
# по значению слова и создаёт итератор
#
#
#
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print "%s%s%d" % (current_word, separator, total_count)
        except ValueError:
            # count was not a number, so silently discard this item
            pass
 
if __name__ == "__main__":
    main()
 
