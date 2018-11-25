#!/usr/bin/env bash

IN_ENCODING='cp866'

iconv -f "${IN_ENCODING}" < "${1}" | less
