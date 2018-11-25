# -*- coding: utf8 -*-
# @Author: Alexander Sharov

from vigenere.encoder import encode
from vigenere.decoder import decode


PROJECT_BASE_DIR = '/Users/asharov/projects/personal/methods-of-information-protection'

ENCODING_MSG = 'сова на пне'
ENCODING_KEY = 'шерлок'


def main():
    encoded_msg = encode(ENCODING_MSG, ENCODING_KEY)
    print(encoded_msg)
    decoded_msg = decode(encoded_msg, ENCODING_KEY)
    print(decoded_msg)


if __name__ == "__main__":
    main()
