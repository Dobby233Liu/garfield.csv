import re
import csv
import sys
import traceback
from quirk_fixer import find_first_comicid_quirkfix

def find_first_comicid(line):
    fix = find_first_comicid_quirkfix(line)
    if fix != None:
        return fix

    try:
        # QUIRK: dataset has a spew of typos and oddities, so the regex has to be complex
        # [0] [0] full id [1] comic [2] nothing [3] sep
        result = re.findall(
            r"^((g[as]|dr|pg|sh|[0-9]+)[0-9a-zA-Z-]+)(\s|)(--|- -|..|. .|\*\*|\* \*)( |)",
            line,
            flags=re.I,
        )
        # raise IndexError(result[0])

        if len(result) <= 0:
            raise IndexError("No match for regex", result, line)
        if len(result[0]) <= 0:
            raise IndexError(
                "No group in match 0 in regex (undefined behaviour)", result[0], line
            )

        return result[0]
    except Exception as e:
        raise IndexError("Can't find comicid") from e

def cleanup(input_file, output):

    def line_iterator(f):
        line = True
        while line:
            line = f.readline().strip()
            yield line
        return
    f = line_iterator(input_file)
    
    writer = csv.writer(output)
    writer.writerow(["transcript", "comic_id"])

    intro = True
    introline_invaild = False
    _proc_line = ""
    comicid = ("", "", "", "", "")

    for line in f:
        print(line)
        raise Exception("l")
        if line == ("-" * len(line)) or line == ("." * len(line)):
            continue

        _sub_comicid = ("", "", "", "", "")

        # search for comicid
        try:
            if intro:
                _sub_comicid = comicid = find_first_comicid(line)
            else:
                _sub_comicid = find_first_comicid(line)
        except IndexError as e:
            if intro:
                introline_invaild = True
            elif not introline_invaild:
                continue
            traceback.print_exc(file=sys.stderr)
            print("\n\nLine text:\n%s" % line, file=sys.stderr)
            print("-" * 20, file=sys.stderr)

        if not intro and comicid[0] != _sub_comicid[0]: 
            # postprocessing - write and reset EVERYTHING
            def splitline(text):
                # Lazier but works version - revert further if problematic
                text = re.sub(r"(\s+|^)-", "\n", text, flags=re.I).strip()
                arr = text.splitlines()
                text = "\n".join(list(map(lambda x: "- " + x.strip(), arr)))
                return text.strip()
            _proc_line = splitline(_proc_line)
            _proc_line = re.sub("(\s)+", r"\1", _proc_line)
            writer.writerow(
                [_proc_line, comicid[0]]
            )  # NOTE: this accounts for gpt-2-simple, which reads [0] only for csvs
            intro = True
            introline_invaild = False
            _proc_line = ""
            comicid = ("", "", "", "", "")
            continue

        _proc_line += line[
            (
                _sub_comicid[5]
                if len(_sub_comicid) >= 6 and _sub_comicid[5] > -1
                else len(
                    _sub_comicid[0]
                    + _sub_comicid[2]
                    + _sub_comicid[3]
                    + _sub_comicid[4]
                )
            ) :
        ]

        intro = False

    return
