# -*- coding: utf8 -*-
# @Author: Alexander Sharov

from vigenere.matrix import generate_vigenere_matrix, generate_msg2key


def decode(message, key):
    enc_mtx = generate_vigenere_matrix(key)
    msg2key_mtx = generate_msg2key(message, key)

    decoded_msg = ''

    for index in range(0, len(message)):
        char1 = msg2key_mtx[0][index]
        char2 = msg2key_mtx[1][index]

        if char1 != ' ':

            char1_ind = 0
            char2_ind = 0

            for line, ind in zip(enc_mtx, range(len(enc_mtx))):
                if line[0] == char2:
                    char2_ind = ind
                    break

            for char, jnd in zip(enc_mtx[char2_ind], range(len(enc_mtx[0]))):
                if char == char1:
                    char1_ind = jnd
                    break
            decoded_msg += enc_mtx[0][char1_ind]

        else:
            decoded_msg += ' '

    return decoded_msg
