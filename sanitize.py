import csv, sys, traceback

ids = []
tsrts = {}
bad = False
reject = False
num = 0

# def eprint(*args, **kwargs):
#  print('', end='', flush=True, file=sys.stdout)
#  print('', end='', flush=True, file=sys.stderr)
#  print(*args, **kwargs, file=sys.stderr)
eprint = print

with open(sys.argv[1]) as f:
    try:
        c = csv.reader(f)
    except:
        bad = True
        traceback.print_exc()
        pass
    next(c)  # discard header
    for r in c:
        num += 1
        tbad = False
        magic = r[1].strip()
        if not magic:
            tbad = bad = True
            eprint("strip #%d has falsy magic: '%s'" % (num, r[1]))
        if tsrts.get(magic, None) == None:
            tsrts[magic] = []
        tsrts[magic].append(r[0])
        if ids.count(magic) > 0:
            print(tsrts[magic])
            tbad = bad = True
            eprint("strip '%s' already exists in csv" % magic)
        ids.append(magic)
        if tbad:
            eprint("-" * 20)

if bad:
    eprint("This CSV file has errors.")
else:
    eprint("This CSV file has no errors.")
if reject:
    sys.exit(1 if bad else 0)
elif bad:
    eprint("Ignoring.")
