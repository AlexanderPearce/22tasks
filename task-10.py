# -*- coding: utf-8 -*-

"""
Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.
"""

raw_values = input('Enter numbers separated by commas: ')

split_raw_values = raw_values.split(',')
int_values = map(int, split_raw_values)
lst_values = list(int_values)
tlp_values = tuple(lst_values)

print('List: ', lst_values)
print('Tuple: ', tlp_values)

