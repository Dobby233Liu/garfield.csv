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

orig = []
with open(sys.argv[1][:-3]+"txt") as of:
    orig = of.readlines()
# Big hax
def print_related_lines(line):
    signatures = list(map(lambda x: x.lstrip("- "), line.splitlines()))
    for _i in range(len(orig)):
        for ii in signatures:
            if ii in i and i.startswith(oldcmid):
                eprint("\n")
                eprint(orig[_i-1], end='')
                eprint(orig[_i], end='')
                eprint(orig[_i+1], end='')
                break

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
            for i in tsrts[magic]:
                print_related_lines(i)
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
