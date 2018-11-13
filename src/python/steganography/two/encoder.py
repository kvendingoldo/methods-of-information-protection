# -*- coding: cp866 -*-
# @Author: Alexander Sharov

import codecs


def encode(encoding, container_file, secret_msg, output_file):
    with codecs.open(container_file, 'r', encoding=encoding) as f:
        data = f.read()

    state = 0
    for byte in secret_msg.encode(encoding):
        for bit in bin(byte)[2:].zfill(8):
            position = data.find(' ', state)
            if bit == '1':
                data = data[:position + 1] + ' ' + data[position + 1:]
            state = position + 2

    with codecs.open(output_file, 'w', encoding=encoding) as f:
        f.write(data)
