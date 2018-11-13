# -*- coding: cp866 -*-
# @Author: Alexander Sharov

import codecs


from steganography.three.analogue import rus2eng


def replace(encoding, index, data):
    processed_data = data

    for char in data[index:]:
        if str(char) in rus2eng:

            encoded_char=str(rus2eng[char]).encode(encoding).decode(encoding)
            processed_data = processed_data[:index - 1] + encoded_char + processed_data[index:]
            print(processed_data)
        index += 1
    return index, processed_data


def encode(encoding, container_file, secret_msg, output_file):
    with codecs.open(container_file, 'r', encoding=encoding) as f:
        data = f.read()

    index = 0

    for byte in secret_msg.encode(encoding):
        for bit in bin(byte)[2:].zfill(8):
            if bit == '1':
                index, data = replace(encoding, index, data)
            else:
                index += 1

    with codecs.open(output_file, 'w', encoding=encoding) as f:
        f.write(data)
