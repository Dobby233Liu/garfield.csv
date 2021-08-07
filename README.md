# garfield.csv
Scripts for Python 3 that helps converting comic transcripts
from [john.ccac.rwth-aachen.de](http://john.ccac.rwth-aachen.de:8000/ftp/dilbert/) to CSV files.

## Pre-converted files
[![.github/workflows/generate.yml](https://github.com/Dobby233Liu/garfield.csv/actions/workflows/generate.yml/badge.svg)](https://github.com/Dobby233Liu/garfield.csv/actions/workflows/generate.yml)

Pre-built files are provided on [gh-pages](https://github.com/Dobby233Liu/garfield.csv/tree/gh-pages) branch, thus also [online](https://dobby233liu.github.io/garfield.csv/) for file downloading. [Source code](.github/workflows/generate.yml) for the workflow that drives this. Files are rebuilt at 00:05 UTC+2 every day.

## Modules

### `enc_convert`
This script converts a text file with a encoding to a text file with another encoding.

Syntax:
```bash
python enc_convert.py <old_file> <new_file> [old_enc|detect] [new_enc|utf-8] [fallback_for_detect|ISO-8859-1]
```
`enc`s have to be a string pointing to a encoding that Python supports.
Using `detect` as `old_enc` requires `chardet` to be installed.
`fallback_for_detect` will be a placeholder when the detecting process goes badly (errors out/has low confindenity).

Run this on a original script file downloaded from John (the server) to correctly run the script through `main`.
(You may don't need to use this; Workflow job has been changed to use iconv instead)

### `main`
The CLI. Specify `-h` as a argument while running this script to get help.
Outputs a CSV file ready for `gpt-2-simple` usage and general parsing/querying/listing/reading/etc.

### `convert`
The module that is used internally by `main`.

### `sanitize`
The script to sanitize the output CSV file. You should not use it.
