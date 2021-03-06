# -*- coding: utf8 -*-
# @Author: Alexander Sharov

from two.analys import find_files

# from one.signatures_dict import get_signatures_dict

PROJECT_BASE_DIR = '/Users/asharov/projects/personal/methods-of-information-protection'

SIGNATURE = b'ABCDEFGK'
    #b'\xed\xab\xee\xdb'

# IN_SIGNATURES = PROJECT_BASE_DIR + '/resources/antivirus_protection/signatures.json'
DIRECTORY_FOR_SEARCH = '/Users/asharov/Downloads/search'
OUT_RESULT_FILE = PROJECT_BASE_DIR + '/out/antivirus_protection/result.txt'


def main():
    # find_files(get_signatures_dict(IN_SIGNATURES), DIRECTORY_FOR_SEARCH, OUT_RESULT_FILE)
    find_files(SIGNATURE, DIRECTORY_FOR_SEARCH, OUT_RESULT_FILE)


if __name__ == "__main__":
    main()
