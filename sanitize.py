import csv, sys, traceback

ids = []
tsrts = {}
bad = False
numbad = False
reject = True
extracheck = False
num = 0

# def eprint(*args, **kwargs):
#  print('', end='', flush=True, file=sys.stdout)
#  print('', end='', flush=True, file=sys.stderr)
#  print(*args, **kwargs, file=sys.stderr)
eprint = print

orig = []
with open(sys.argv[1][:-3] + "txt") as of:
    orig = of.readlines()
# Big hax
def print_related_lines(line, comicid):
    signatures = list(map(lambda x: x.lstrip("- "), line.splitlines()))
    for _i in range(len(orig)):
        i = orig[_i]
        success = False
        for ii in signatures:
            if ii in i and i.strip().startswith(comicid):
                eprint("")
                eprint(orig[_i - 1], end="")
                eprint(orig[_i], end="")
                eprint(orig[_i + 1], end="")
                success = True
                break
        if success:
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
                print_related_lines(i, magic)

        if not (magic[:2] == "pg" or magic[:2] == "sh"):
            try:
                if int(magic[-2:]) > 31 or int(magic[-2:]) < 1:
                    tbad = bad = True
                    eprint("strip '%s' 's day is invaild" % magic)
                    print(tsrts[magic])
            except Exception: pass
            try:
                if int(magic[-4:-2]) > 12 or int(magic[-4:-2]) < 1:
                    tbad = bad = True
                    eprint("strip '%s' 's month is invaild" % magic)
                    print(tsrts[magic])
            except Exception: pass

        if extracheck and magic.startswith("ga") and len(tsrts[magic][-1].splitlines()) < 3:
            tbad = bad = True
            numbad = True
            eprint("strip '%s' has lesser than 3 lines" % magic)

        ids.append(magic)
        if tbad:
            eprint("-" * 20)

if bad:
    eprint("This CSV file has errors.")
else:
    eprint("This CSV file has no errors.")
if numbad:
    eprint("Detected abnormal number of lines. This may be a false positive, since it can be a dataset issue.")
if reject:
    sys.exit(1 if bad else 0)
elif bad:
    eprint("Ignoring.")
