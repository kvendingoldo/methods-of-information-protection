# -*- coding: utf8 -*-
# @Author: Alexander Sharov

from vigenere.matrix import generate_vigenere_matrix, generate_msg2key


def encode(message, key):
    enc_mtx = generate_vigenere_matrix(key)
    msg2key_mtx = generate_msg2key(message, key)

    encoded_msg = ''

    for index in range(0, len(message)):
        char1 = msg2key_mtx[0][index]
        char2 = msg2key_mtx[1][index]

        char1_ind = 0
        char2_ind = 0

        if char1 != ' ':
            for char, jnd in zip(enc_mtx[0], range(len(enc_mtx[0]))):
                if char == char1:
                    char1_ind = jnd
                    break

            for line, ind in zip(enc_mtx, range(len(enc_mtx))):
                if line[0] == char2:
                    char2_ind = ind
                    break

            encoded_msg += enc_mtx[char2_ind][char1_ind]
        else:
            encoded_msg += ' '

    return encoded_msg
