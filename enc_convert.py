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
  from chardet.universaldetector import UniversalDetector
  ret = {"lord": "latin-1"} # LORD latin-1
  detector = UniversalDetector()
  with open(args[0], "r", encoding="latin-1") as f: # encoding="ascii", errors="surrogateescape"
    for line in f.readlines():
      detector.feed(line)
      if detector.done:
        break
  detector.close()
  ret = ret.result
  print(ret)
  ret = ret["encoding"]
  return ret

enc = input_enc()
with open(sys.argv[1], "rb") as f:
  with open(sys.argv[2], "wb") as w:
    while (b := f.read(1)):
        w.write(b.decode(enc).encode(sys.argv[4]))
