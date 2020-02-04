# -*- coding: utf-8 -*-

"""
Нужно проверить, все ли числа в последовательности уникальны.
"""

base_list = [1, 30, 25, 150, 45, 200, 15, 1]

if len(base_list) == len(set(base_list)):
    print('All numbers are unique')
else:
    print('Some numbers not unique')
