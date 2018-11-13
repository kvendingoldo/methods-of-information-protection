# -*- coding: cp866 -*-
# @Author: Alexander Sharov

import codecs


def decode(encoding, input_file, output_file):
    with codecs.open(input_file, 'r', encoding=encoding) as f:
        lines = [line for line in f.read().splitlines()]

    byte_str = ''
    decoded_message = bytearray()

    for index in range(len(lines)):
        last_character = lines[index][-1]

        if last_character == ' ':
            byte_str += '1'
        else:
            byte_str += '0'

        if len(byte_str) == 8:
            byte = int(byte_str, 2)
            if byte == 0:
                break
            else:
                decoded_message.append(byte)
                byte_str = ''

    with codecs.open(output_file, 'w', encoding=encoding) as f:
        f.write(decoded_message.decode(encoding))
