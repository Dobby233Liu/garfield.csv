import csv, sys

ids = []

with open(sys.argv[1]) as f:
    c = csv.reader(f)
    next(c) # discard header
    for r in c:
      try:
        magic = r[1]
        if ids.count(magic) > 0:
            raise IndexError("comic '%s' already exists in csv" % magic)
        ids.append(magic)
      except IndexError as e:
        print(e)
        print("-"*20)
