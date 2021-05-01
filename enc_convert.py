"""
Just portable iconv

Usage:
python3 enc_convert.py _garfield.txt garfield.txt latin-1 utf-8 ISO-8859-1

Convert with this tool before throwing it to main.py
"""

import sys

args = [sys.argv[1], sys.argv[2], "detect", "utf-8", "ISO-8859-1"]
if len(sys.argv) >= 4:
  args[2] = sys.argv[4 - 1]
if len(sys.argv) >= 5:
  args[3] = sys.argv[5 - 1]
if len(sys.argv) >= 6:
  args[4] = sys.argv[6 - 1]

def input_enc(file):
  if args[2] != "detect":
    return args[2]
  try:
    import chardet
    ret = {"lord": "latin-1"} # LORD latin-1
    with open(file, "rb") as f:
      ret = chardet.detect(f.read())
    if ret["confidence"] < 0.6:
      pass
    ret = ret["encoding"]
    return ret
  except:
    pass
  return args[4]

enc = input_enc(args[0])
with open(args[0], "rb") as f:
  with open(args[1], "wb") as w:
    while (b := f.read(1)):
      try:
        w.write(b.decode(enc).encode(args[3]))
      except UnicodeDecodeError as e:
        print(e)
