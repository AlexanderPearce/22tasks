# -*- coding: utf-8 -*-

"""
Напишите программу для слияния нескольких словарей в один.
"""

a = {"a": 1, "b": 4, "c": 3, "d": 2}
b = {"e": 5, "f": 6, "g": 7, "h": 8}


def dict_update(d1, d2):
    d1.update(d2)
    return a

print(dict_update(a, b))
# -----------------------OR--------------------------
result = {}

for d in (a, b):
    result.update(d)

print(result)
