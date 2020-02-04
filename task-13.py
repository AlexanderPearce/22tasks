# -*- coding: utf-8 -*-

"""
При заданном целом числе n посчитайте n + nn + nnn
n^1+n^2+n^3......n^k
"""

number = int(input('Input Number: '))

sum_exp = 0

for exp in range(1, number+1):
    sum_exp += number ** exp

print(sum_exp)

# -------------------meant it-------------------------------


def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)


solve(5)
