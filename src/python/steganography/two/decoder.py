# -*- coding: cp866 -*-
# @Author: Alexander Sharov

import codecs
import re


def decode(encoding, input_file, output_file):
    with codecs.open(input_file, 'r', encoding=encoding) as f:
        data = f.read()

    decoded_message = bytearray()
    byte_str = ''

    for space in re.findall(' +', data):
        byte_str += str(len(space) - 1)

        if len(byte_str) == 8:
            byte = int(byte_str, 2)
            if byte == 0:
                break
            else:
                decoded_message.append(byte)
                byte_str = ''

    with codecs.open(output_file, 'w', encoding=encoding) as f:
        f.write(decoded_message.decode(encoding))
