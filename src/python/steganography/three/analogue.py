# -*- coding: cp866 -*-
# @Author: Alexander Sharov


def get_rus2eng():
    rus2eng = {
        ' ': 'a',
        'Ĩ': 'e',
        'Ē': 'k',
        'Ŧ': 'm',
        'Ž': 'o',
        'ā': 'p',
        'á': 'c',
        'ã': 'y',
        'å': 'x',
        '': 'A',
        '': 'E',
        '': 'K',
        '': 'M',
        '': 'H',
        '': 'O',
        '': 'P',
        '': 'C',
        '': 'T',
        '': 'Y',
        '': 'X'
    }

    return rus2eng


def get_eng2rus():
    eng2rus = {
        'a': ' ',
        'e': 'Ĩ',
        'k': 'Ē',
        'm': 'Ŧ',
        'o': 'Ž',
        'p': 'ā',
        'c': 'á',
        'y': 'ã',
        'x': 'å',
        'A': '',
        'E': '',
        'K': '',
        'M': '',
        'H': '',
        'O': '',
        'P': '',
        'C': '',
        'T': '',
        'Y': '',
        'X': ''
    }

    return eng2rus


def get_rus_str():
    return ' ĨĒŦŽāáãå'


def get_eng_str():
    return 'aekmopcyxAEKMHOPCTYX'
