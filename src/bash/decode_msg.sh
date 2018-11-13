#!/bin/bash

FILE="${1}"

ENCODING='cp866'

iconv -f "${ENCODING}" < "${FILE}" | less
