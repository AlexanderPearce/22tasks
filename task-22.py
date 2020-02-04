# -*- coding: utf-8 -*-

"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
"""

import collections

text = 'the lazy dog jumped over another lazy dog'
words = text.split()

counter = collections.Counter(words)
most_common, occurrences = counter.most_common()[0]

longest = max(words, key=len)

print(most_common, longest)
