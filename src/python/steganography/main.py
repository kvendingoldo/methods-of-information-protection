# -*- coding: cp866 -*-
# @Author: Alexander Sharov

from three.encoder import encode
from three.decoder import decode

PROJECT_BASE_DIR = '/Users/asharov/projects/personal/methods-of-information-protection'

ENCODING = 'cp866'

IN_FILE_CONTAINER = PROJECT_BASE_DIR + '/resources/steganography/container_cp866.txt'

OUT_FILE_DEC = PROJECT_BASE_DIR + '/out/steganography/decoded.txt'
OUT_FILE_ENC = PROJECT_BASE_DIR + '/out/steganography/encoded.txt'


def main():
    hide_msg = 'A я'
    encode(ENCODING, IN_FILE_CONTAINER, hide_msg, OUT_FILE_ENC)
    decode(ENCODING, OUT_FILE_ENC, OUT_FILE_DEC)


if __name__ == "__main__":
    main()
