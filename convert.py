import re
import csv
import sys
import traceback
from quirk_fixer import find_first_comicid_quirkfix


def splitline(text):
    # Lazier but works version - revert further if problematic
    text = re.sub(r"(\s+|^)-", "\n", text, flags=re.I).strip()
    arr = text.splitlines()
    text = "\n".join(list(map(lambda x: "- " + x.strip(), arr)))
    return text.strip()


def find_first_comicid(line):
    try:
        fix = find_first_comicid_quirkfix(line)
        if fix != None:
            " " + fix[0]
            return fix
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

    writer = csv.writer(output)
    writer.writerow(["transcript", "comic_id"])

    intro = True
    #introline_invaild = False
    _proc_line = ""
    comicid = ("", "", "", "", "")
    _sub_comicid = ("", "", "", "", "")

    for line in line_iterator(input_file):
        if line == ("-" * len(line)) or line == ("." * len(line)):
            continue

        #be_there = False

        # search for comicid
        try:
            _sub_comicid = find_first_comicid(line)
            if intro:
                comicid = _sub_comicid
        except IndexError as e:
            #if intro:
            #    introline_invaild = True
            traceback.print_exc(file=sys.stderr)
            print("\n\nLine text:\n%s" % line, file=sys.stderr)
            print("-" * 20, file=sys.stderr)
            #if not intro and not introline_invaild:
            #    be_there = True

        if comicid[0] != _sub_comicid[0]:# or be_there:
            # postprocessing - write and reset EVERYTHING
            _proc_line = splitline(_proc_line)
            _proc_line = re.sub("(\s)+", r"\1", _proc_line)
            writer.writerow(
                [_proc_line, comicid[0]]
            )  # NOTE: this accounts for gpt-2-simple, which reads [0] only for csvs
            intro = True
            introline_invaild = False
            _proc_line = ""
            try:
                comicid = _sub_comicid = find_first_comicid(line)
            except IndexError as e:
                introline_invaild = True
                traceback.print_exc(file=sys.stderr)
                print("\n\nLine text:\n%s" % line, file=sys.stderr)
                print("-" * 20, file=sys.stderr)

        _proc_line += (" " if not intro else "") + (
            line[
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
        )

        intro = False

    _proc_line = splitline(_proc_line)
    _proc_line = re.sub("(\s)+", r"\1", _proc_line)
    writer.writerow([_proc_line, comicid[0]])

    return
