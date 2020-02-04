# -*- coding: utf-8 -*-

"""
Напишите программу, которая принимает имя файла и выводит его расширение.
"""

from os import listdir
from os.path import isfile, join

base_path = '/home/alexander/PycharmProjects/22tasks/'
filename = input('Input filename: ')

files_list = [f for f in listdir(base_path) if isfile(join(base_path, f))]

for file in files_list:
    if filename == file.split('.')[0]:
        print(file.split('.')[1])
