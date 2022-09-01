# Задача 1. Сисадмин

import os


def print_path_abs(user_file):
    path = os.path.join(os.path.abspath(user_file))
    print('Абсолютный путь до файла:', path)


def print_path(user_file):
    path1 = os.path.abspath(user_file)
    path2 = os.path.abspath('..')
    print('Относительный путь до файла:', ''.join(path1.split(path2)))


i_file = input('Введите имя файла: ')
print_path_abs(i_file)
print_path(i_file)
