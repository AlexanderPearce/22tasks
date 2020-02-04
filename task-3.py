# -*- coding: utf-8 -*-

import operator

"""
Отсортируйте словарь по значению в порядке возрастания и убывания.
dict = {key:value}
"""

d = {"a": 1, "b": 4, "c": 3, "d": 2}

sorted_d_up = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d_up)

sorted_d_down = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d_down)




