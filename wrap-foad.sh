#!/bin/bash

# Requires the Muttils project:
# https://bitbucket.org/blacktrash/muttils
# Python3 port: https://github.com/adversary-org/misc-scripts/python3/muttils3

foad=foad.py
wrap=/usr/local/bin/wrap

exec $foad "$@" | $wrap -w 80
