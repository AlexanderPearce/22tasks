# -*- coding: utf-8 -*-

"""
Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.
"""

ns = input('Enter number system: ')
volue = input('Enter volue: ')

volue = int(volue, int(ns))

print('Number is: ', volue)
