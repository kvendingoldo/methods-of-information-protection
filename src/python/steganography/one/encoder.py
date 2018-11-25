# -*- coding: cp866 -*-
# @Author: Alexander Sharov


def encode(encoding, container_file, secret_msg, output_file):
    with open(container_file, 'r', encoding=encoding) as f:
        lines = f.readlines()

    bits_count = 0
    for byte in secret_msg.encode(encoding):
        for bit in bin(byte)[2:].zfill(8):
            if bit == '1':
                lines[bits_count] = lines[bits_count][:-1] + ' \n'
            bits_count += 1

    with open(output_file, 'w', encoding=encoding) as f:
        for line in lines:
            f.write(line)
