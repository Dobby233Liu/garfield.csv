"""
GUI for the convert module based on argparse.

Usage:

give -h as an argument while running this file
"""

import argparse

parser = argparse.ArgumentParser(description="Translates comic transcripts from john.ccac.rwth-aachen.de to CSV files.",
  epilog="For such transcript in 'data', please see http://john.ccac.rwth-aachen.de:8000/ftp/dilbert/"
)
parser.add_argument("data", type=argparse.FileType('r', encoding="utf-8"), help="Filename for the original transcript")
parser.add_argument("output", type=argparse.FileType('w', encoding="utf-8", newline=''), help="Filename for the CSV output")

from convert import cleanup

if __name__ == "__main__":
  #with sys.stdout if fn == "-" else open(fn, "w", encoding="utf-8", newline='') as w:
    # QUIRK: we don't know the encoding
    #with sys.stdin if datname == "-" else open(datname, 'r', encoding="latin-1") as f:
    #  cleanup(f, w)
  args = parser.parse_args()
  cleanup(args.data, args.output)
