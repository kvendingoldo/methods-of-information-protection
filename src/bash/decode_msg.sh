#!/bin/bash

FILE="${steganography}"

ENCODING='cp866'

iconv -f "${ENCODING}" < "${FILE}" | less
