# -*- coding: cp866 -*-
# @Author: Alexander Sharov

import codecs

from analogue import rus2eng


def decode(encoding, input_file, output_file):
    with codecs.open(input_file, 'r', encoding=encoding) as f:
        data = f.read()

    decoded_message = bytearray()
    byte_str = ''











    with codecs.open(output_file, 'w', encoding=encoding) as f:
        f.write(decoded_message.decode(encoding))
