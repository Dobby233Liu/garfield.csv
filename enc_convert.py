"""
Just portable iconv

Usage:
python3 enc_convert.py _garfield.txt garfield.txt latin-1 utf-8

Convert with this tool before throwing it to main.py
"""

import sys

def input_enc(args=sys.argv[1:]):
  if args[2] != "detect":
    return args[2]
  import chardet
  ret = {"lord": "latin-1"} # LORD latin-1
  with open(args[0], "rb") as f:
    ret = chardet.detect(f.read())
  print(ret)
  if ret["confidence"] < 0.6:
    print("low faith")
    return "latin-1" # lord forever
  ret = ret["encoding"]
  return ret

enc = input_enc()
with open(sys.argv[1], "rb") as f:
  with open(sys.argv[2], "wb") as w:
    while (b := f.read(1)):
      try:
        w.write(b.decode(enc).encode(sys.argv[4]))
      except UnicodeDecodeError as e:
        print(e)
