# garfield.csv
Scripts for Python 3 that helps converting comic transcripts
from [john.ccac.rwth-aachen.de](http://john.ccac.rwth-aachen.de:8000/ftp/dilbert/) to CSV files.

## Pre-converted files
[![.github/workflows/generate.yml](https://github.com/Dobby233Liu/garfield.csv/actions/workflows/generate.yml/badge.svg)](https://github.com/Dobby233Liu/garfield.csv/actions/workflows/generate.yml)

Provided on [gh-pages](https://github.com/Dobby233Liu/garfield.csv/tree/gh-pages) branch.

## Modules

### `enc_convert`
Converts a text file with a encoding to a text file with another encoding.

Syntax:
```bash
python enc_convert.py <old_file> <new_file> [old_enc|detect] [new_enc|utf-8] [fallback_for_detect|ISO-8859-1]
```
`enc`s have to be a string pointing to a encoding that Python supports.
`detect` as `old_enc` requires `chardet` to be installed.
`fallback_for_detect` will be a placeholder when the detecting process goes badly.

### `main`
Specify `-h` as a argument while running this script to get help.

### `convert`
Module used internally by `main`.
