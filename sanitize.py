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
def guess_actual_comicid(line, oldcmid, ids):
    signatures = list(map(lambda x: x.lstrip("- "), line.splitlines()))
    guess = None
    orig_line = None
    prev_line = None
    for _i in range(len(orig)):
        i = orig[_i]
        for ii in signatures:
            if ii in i and i.startswith(oldcmid):
                orig_line = i
                prev_line = lastline = orig[_i-1]
                #nextline = orig[_i+1]
                lastcmid = lastline[:len(oldcmid)]
                l = str(int(lastcmid[-2:])+1)
                if len(l)<2:
                    l = "0"+l
                guess = oldcmid[:-2] + l
                if guess in ids:
                    guess = "a contiunation of "+lastcmid
                break
    if guess:
        eprint("\nTried to guess, it may actually be "+guess+" (check it yourselves, don't rely on me)")
        eprint("Original line in txt file?: \n"+orig_line,end='')
        eprint("Prev line in txt file?: \n"+prev_line,end='')

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
            guess_actual_comicid(r[0], r[1], ids)
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
