# -*- coding: utf-8 -*-

"""
Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
"""

main_list = [1, 2, 3, 4, 56, 53, 234, 8, 33, 89, 237, 357, 22]

for element in main_list:
    if element == 237:
        break
    elif element % 2 == 0:
        print(element)
