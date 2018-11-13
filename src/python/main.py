# -*- coding: cp866 -*-
# @Author: Alexander Sharov

from steganography.three.encoder import encode
#from steganography.three.decoder import decode

ENCODING = 'cp866'
FILE_DEC = '../../out/decoded.txt'
FILE_ENC = '../../out/encoded.txt'
FILE_CONTAINER = '../../resources/container.txt'


def main():
    hide_msg = 'A я'
    encode(ENCODING, FILE_CONTAINER, hide_msg, FILE_ENC)
    #decode(ENCODING, FILE_ENC, FILE_DEC)


if __name__ == "__main__":
    main()
