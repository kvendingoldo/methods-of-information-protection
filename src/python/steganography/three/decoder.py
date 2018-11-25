# -*- coding: cp866 -*-
# @Author: Alexander Sharov

import re

from three.analogue import get_eng2rus
from three.analogue import get_eng_str, get_rus_str


def decode(encoding, input_file, output_file):
    with open(input_file, 'r', encoding=encoding) as f:
        data = f.read()

    decoded_message = bytearray()
    byte_str = ''

    allowed_alphabet = re.finditer('[' + get_rus_str() + get_eng_str() + ']', data)

    eng2rus = get_eng2rus()

    while True:
        try:
            match = next(allowed_alphabet)
        except StopIteration:
            break
        if data[match.start()] in eng2rus:
            byte_str += '1'
        else:
            byte_str += '0'
        if len(byte_str) == 8:
            byte = int(byte_str, 2)
            byte_str = ''
            if byte == 0:
                break
            decoded_message.append(byte)

    with open(output_file, 'w', encoding=encoding) as f:
        f.write(decoded_message.decode(encoding))
