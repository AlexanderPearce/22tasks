# -*- coding: utf-8 -*-

"""
Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
"""

import time

time_value = time.strftime('%d:%H:%M:%S', time.localtime())
print(time_value)

# -------------------meant it-------------------------------


def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')


convert(1234565)
