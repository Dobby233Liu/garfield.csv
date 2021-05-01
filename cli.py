"""
Seperate maintainence file for the CLI based on argparse.

Usage:

from .cli import parser
args = parser.parse_args()
[...]
"""

import argparse

parser = argparse.ArgumentParser(description="Translates comic transcripts from john.ccac.rwth-aachen.de to CSV files.",
  epilog="For such transcript in 'data', please see http://john.ccac.rwth-aachen.de:8000/ftp/dilbert/"
)
parser.add_argument("data", type=argparse.FileType('r'), help="Filename for the original transcript")
parser.add_argument("output", type=argparse.FileType('w', encoding="utf-8"), help="Filename for the CSV output")
