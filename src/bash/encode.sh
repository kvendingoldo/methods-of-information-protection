#!/usr/bin/env bash

IN_ENCODING='utf8'
OUT_ENCODING='cp866'

iconv -f "${IN_ENCODING}" -t "${OUT_ENCODING}" "${1}" > "${2}"