# -*- coding: utf8 -*-
# @Author: Alexander Sharov

import numpy as np


def generate():
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
                'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    return np.array([alphabet[ind:] + alphabet[:ind] for ind in range(0, 33)])


def generate_vigenere_matrix(key):
    matrix = generate()

    enc_matrix = [matrix[0]]
    for char in key:
        for line in matrix[1:]:
            if char == line[0]:
                enc_matrix += [line]

    return np.array(enc_matrix)


def generate_msg2key(message, key):
    msg2key = [[], []]
    index = 0
    for char in message:
        msg2key[0].append(char)
        if char != ' ':
            msg2key[1].append(key[index % len(key)])
            index += 1
        else:
            msg2key[1].append(' ')

    return np.array(msg2key)


def get_alphabet():
    return ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
