# -*- coding: utf8 -*-
# @Author: Alexander Sharov

import os
import re
import fnmatch
import codecs


def files_within(directory_path, pattern="*"):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for file_name in fnmatch.filter(filenames, pattern):
            yield os.path.join(dirpath, file_name)


def find_files(signature, directory, result_file):
    result_list = []
    for file_path in files_within(directory):
        with open(file_path, mode='rb') as f:
            if re.search(signature, f.read()):
                result_list.append(file_path)

    with open(result_file, 'w') as f:
        for result in result_list:
            f.write(result + '\n')
