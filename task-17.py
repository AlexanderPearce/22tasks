# -*- coding: utf-8 -*-

"""
Сложите цифры целого числа.
"""

number_str = input('Input number: ')
summ = 0

for i in list(number_str):
    summ += int(i)

print(summ)
# ---------------------------OR--------------------------


def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)


print(sum_digits(55))
