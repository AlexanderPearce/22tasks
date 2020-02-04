# -*- coding: utf-8 -*-

"""
С помощью анонимной функции извлеките из списка числа, делимые на 15.
"""

base_list = [1, 30, 25, 150, 45, 200, 15]


filtered_list = list(filter(lambda x: x % 15 != 0, base_list))

print(filtered_list)
