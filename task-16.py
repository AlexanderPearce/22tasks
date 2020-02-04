# -*- coding: utf-8 -*-

"""
Выведите список файлов в указанной директории.
"""

from os import listdir
from os.path import isfile, join

base_path = '/home/alexander/PycharmProjects/22tasks/'

files_list = [f for f in listdir(base_path) if isfile(join(base_path, f))]
print(files_list)
