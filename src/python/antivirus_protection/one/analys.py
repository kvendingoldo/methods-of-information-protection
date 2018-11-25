# -*- coding: utf8 -*-
# @Author: Alexander Sharov

import codecs
import os
import fnmatch


def files_within(directory_path, pattern="*"):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for file_name in fnmatch.filter(filenames, pattern):
            yield os.path.join(dirpath, file_name)


def find_files(signatures, directory, result_file):
    result_list = []
    for file_path in files_within(directory):
        # читаем первые 32 символа
        with open(file_path, mode='rb') as f:
            file = f.read(32)
        # переводим в шестнадцатеричную систему
        hex_bytes = " ".join(['{:02X}'.format(byte) for byte in file])

        for element in signatures:
            for signature in element["signature"]:
                # Поскольку наши байты представлены в виде строки, и за байт отвечает два символа, мы умножаем смещение на antivirus_protection и добавляем количество пробелов между "байтами".
                offset = element["offset"] * 2 + element["offset"]
                if signature == hex_bytes[offset:len(signature) + offset].upper():
                    result_list.append(file_path)

    with codecs.open(result_file, 'w') as f:
        for result in result_list:
            f.write(result + '\n')
