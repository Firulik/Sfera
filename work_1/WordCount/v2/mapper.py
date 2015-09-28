#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Более сложный  Mapper, использующий Итераторы и генераторы Питона"""
 
import sys, re
 
# эта функция вернёт своебразный "массив массивов"
def read_input(file):
    splitter = re.compile('\W*')
    for line in file:
        # разбивает строку на слова
        yield line.split()  # возвращает генератор
 
"""Точка входа в мэппер с разделителем в виде таба в качестве разделителя по-умолчанию."""
def main(separator='\t'):
    # Передаём в качестве "файла" стандартный поток ввода
    data = read_input(sys.stdin)
    for words in data:
        # Пишем результаты в стандартный поток вывода
        # what we output here will be the input for the Выход мэппера будет входом редуктора
        # Reduce step, i.e. the input for reducer.py
        #
        # отделяем слово  табом от формального
# ("формального" так как сумма ещё не подсчитана - это будет сделано в редукторе)
# числа вхождений равного 1 
        for word in words:
	    print '%s%s%d' % (word, separator, 1)
 
if __name__ == "__main__":
    main()
