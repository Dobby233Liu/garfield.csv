import re
import csv
import sys
import traceback
from quirk_fixer import find_first_comicid_quirkfix

def stripm(text):
  
  arr = text.splitlines()
  ret = ""
  
  for i in arr:
    ret = ret + i.strip() + "\n"
    
  ret = ret.strip()
  
  return ret

def find_first_comicid(line, ln=None):

  fix = find_first_comicid_quirkfix(line)
  if fix != None:
    return fix

  try:
    
    # QUIRK: dataset has a spew of typos and oddities, so the regex has to be complex
    # [0] [0] full id [1] comic [2] nothing [3] sep
    result = re.findall(r'^((g[as]|dr|pg|sh|[0-9]+)[0-9a-zA-Z-]+)(\s|)(--|- -|..|. .|\*\*|\* \*)', line, flags=re.I)
    #raise IndexError(result[0])

    if len(result) <= 0:
      raise IndexError("No match for regex", result, line)
    if len(result[0]) <= 0:
      raise IndexError("No group in match 0 in regex (undefined behaviour)", result[0], line)

    return result[0]
  
  except Exception as e:
    
    raise IndexError("Can't find comicid for line number %s" % ln) from e

def cleanup(input_file, output):
  
  lines = input_file.readlines() # WARNING: this is bad, but is fine for now
  writer = csv.writer(output)
  
  writer.writerow(["transcript", "comic_id"])

  _skip_ahead = 0

  for i in range(len(lines)):
    
    if _skip_ahead >= 1:
      _skip_ahead = _skip_ahead - 1
      continue
    
    line = lines[i].strip()
    if (line == ("-" * len(line)) or line == ("." * len(line))):
      continue
    
    # find comicid for intro line first (for merging lines together)
    introline_invaild = False
    comicid = ("", "", "", "")
    try:
      comicid = find_first_comicid(line, ln=i)
    except IndexError as e:
      introline_invaild = True
      traceback.print_exc(file=sys.stderr)
      print("\n(While parsing intro line. Line:)\n%s" % line, file=sys.stderr)
      # line = " " + ""
      print("-"*20, file=sys.stderr)
    
    _proc_line = ""
    
    # hack to merge lines to one 
    for i2 in range(len(lines) - i):
      _loop_line = lines[i + i2].strip()
      if ((_loop_line == "-" * len(_loop_line)) or _loop_line == ("." * len(_loop_line))):
        _skip_ahead += 1
        continue

      _sub_comicid = ("", "", "", "")
      try:
        _sub_comicid = find_first_comicid(_loop_line, ln=i + i2)
      except IndexError as e:
        if not introline_invaild:
          break
        if i2 > 0:
          traceback.print_exc(file=sys.stderr)
          print("\n(While parsing secondary lines. Line:)\n%s" % _loop_line, file=sys.stderr)
        _loop_line = " " + _loop_line
        if i2 > 0:
          print("-" * 20, file=sys.stderr)
      if comicid[0] != _sub_comicid[0]:
        break

      if i2 == 0:
        _proc_line += "-"
      _proc_line += _loop_line[len(_sub_comicid) >= 5 ? _sub_comicid[4] : len(_sub_comicid[0]+_sub_comicid[2]+_sub_comicid[3]):]

      if i2 > 0:
        _skip_ahead += 1

    _proc_line = re.sub("(\s)+", r"\1", _proc_line)
    # fix
    _proc_line = "\n- ".join(_proc_line.split("- "))
    _proc_line = "\n- ".join(_proc_line.split(" -"))
    _proc_line = " ->".join(_proc_line.split("\n- >")) # FIXME: sus
    _proc_line = stripm(_proc_line)

    writer.writerow([_proc_line, comicid[0]]) # NOTE: this accounts for gpt-2-simple, which reads [0] only for csvs
    
  return
