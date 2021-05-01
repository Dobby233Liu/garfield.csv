"""
Just portable iconv

Usage:
python3 enc_convert.py _garfield.txt garfield.txt latin-1 utf-8

Convert with this tool before throwing it to main.py
"""

import sys

with open(sys.argv[1], "rb") as f:
  with open(sys.argv[2], "wb") as w:
    while (b := f.read(1)):
        w.write(b.decode(sys.argv[3]).encode(sys.argv[4]))
