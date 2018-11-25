# -*- coding: cp866 -*-
# @Author: Alexander Sharov

import re

from three.analogue import get_rus2eng
from three.analogue import get_rus_str


def replace(rus2eng, data, index):
    for char in data[index:]:
        if char in rus2eng:
            return data[:index] + rus2eng[char] + data[index + 1:]


def encode(encoding, container_file, secret_msg, output_file):
    rus2eng = get_rus2eng()

    with open(container_file, 'rb') as f:
        data = f.read().decode(encoding)

    allowed_alphabet = re.finditer('[' + get_rus_str() + ']', data)

    for byte in secret_msg.encode(encoding):
        for bit in bin(byte)[2:].zfill(8):
            iter = next(allowed_alphabet)
            if bit == '1':
                data = replace(rus2eng, data, iter.start())

    with open(output_file, 'w', encoding=encoding) as f:
        f.write(data)
