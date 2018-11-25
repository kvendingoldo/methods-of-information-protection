# -*- coding: cp866 -*-
# @Author: Alexander Sharov


def get_rus2eng():
    rus2eng = {
        'а': 'a',
        'е': 'e',
        'к': 'k',
        'м': 'm',
        'о': 'o',
        'р': 'p',
        'с': 'c',
        'у': 'y',
        'х': 'x',
        'А': 'A',
        'Е': 'E',
        'К': 'K',
        'М': 'M',
        'Н': 'H',
        'О': 'O',
        'Р': 'P',
        'С': 'C',
        'Т': 'T',
        'У': 'Y',
        'Х': 'X'
    }

    return rus2eng


def get_eng2rus():
    eng2rus = {
        'a': 'а',
        'e': 'е',
        'k': 'к',
        'm': 'м',
        'o': 'о',
        'p': 'р',
        'c': 'с',
        'y': 'у',
        'x': 'х',
        'A': 'А',
        'E': 'Е',
        'K': 'К',
        'M': 'М',
        'H': 'Н',
        'O': 'О',
        'P': 'Р',
        'C': 'С',
        'T': 'Т',
        'Y': 'У',
        'X': 'Х'
    }

    return eng2rus


def get_rus_str():
    return 'аекморсухАЕКМНОРСТУХ'


def get_eng_str():
    return 'aekmopcyxAEKMHOPCTYX'
