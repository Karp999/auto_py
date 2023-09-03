# Задание №1:
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
# Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# Доработать проект, добавив тест команды расчёта хеша (h). 
# Проверить, что хеш совпадает с рассчитанным командой crc32.

import task1_dz1
import sum_crc32

falderin = '/home/user/tst'
falderout = '/home/user/out'


def test_1_find_text_in_command():
    # семинар
    assert task1_dz1.find_text_in_command(f'cd {falderin}; 7z a {falderout}/arh1',
                                   'Everything is Ok'), 'test1 FAIL'


def test_2_find_text_in_command():
    #  проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
    assert task1_dz1.find_text_in_command(f'ls {falderout}',
                                   'arh1.7z'), 'test2 FAIL'


def test_3_find_text_in_command():
    #  тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.
    temp = sum_crc32.crc32(f'{falderout}/arh1.7z').lower()
    assert task1_dz1.find_text_in_command(f'crc32 {falderout}/arh1.7z',
                                   temp), 'test3 FAIL'