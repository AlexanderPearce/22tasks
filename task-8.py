# -*- coding: utf-8 -*-

"""
Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза,
которые одинаково читаются слева направо и справа налево.
"""

word = input('Enter the word: ')
word_revers = word[::-1]

if word == word_revers:
    print('This is a palindrome')
else:
    print('This is NOT a palindrome')
