import csv, sys

exists = {}

with open(sys.argv[1]) as f:
    c = c.DictReader(f)
    for r in c:
      magic = "comic_" + r["comic_id"]
      if exists[magic]:
        raise IndexError("comic '%s' already exists in csv" % r["comic_id"]
      exists[magic] = True
