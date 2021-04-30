import re
import csv

def stripm(text):
  arr = text.splitlines()
  _ = ""
  for i in arr:
    __ = i.strip()
    _ = _ + __ + "\n"
  _ = _.strip()
  return _

def _find_first_comicid(line, ln=None):
  try:
    result = re.findall(r'^(\s|)((g[as]\w+)(\s|)(--|\.\.))', line)
    if len(result) <= 0:
      raise IndexError("no match for regex", result, line)
    if len(result[0]) <= 0:
      raise IndexError("no group in match 0 (???)", result[0], line)

    return result[0][1:]
  except Exception as e:
    raise IndexError("can't find comicid for line (line number %s)" % ln) from e

def cleanup(input_file, output):
  lines = input_file.readlines()
  writer = csv.writer(output)

  _skip_ahead = 0

  for i in range(len(lines)):
    # Skip-ahead
    if _skip_ahead >= 1:
      _skip_ahead = _skip_ahead - 1
      continue
    
    # find comicid (for merging megahack)
    comicid = _find_first_comicid(lines[i], ln=i)
    
    _proc_line = ""
    # megahack to merge lines to one
    for i2 in range(len(lines) - i):
      _loop_line = lines[i + i2].strip()
      _sub_comicid = []
      try:
        _sub_comicid = _find_first_comicid(_loop_line, ln=i + i2)
      except: # line has no comicid header
        _proc_line += " " + _loop_line
        _skip_ahead += 1
        continue
      
      if _sub_comicid[1] != comicid[1]:
        break

      #if comicid[1] == "ga210214":
      #  print(_proc_line)
      #  print(_loop_line)     
      if i2 == 0:
        _proc_line += "-"
      _proc_line += _loop_line[len(comicid[0]):]
      if i2 != 0:
        _skip_ahead += 1
    
    # Final processing
    #if "catburger" in _proc_line or comicid[1] == "ga210214":
    #  print(_proc_line)
    _proc_line = re.sub("(\s)+", r"\1", _proc_line)
    #_proc_line = re.sub("- -", "-  -", _proc_line)
    _proc_line = "\n- ".join(_proc_line.split("- "))
    _proc_line = stripm(_proc_line)
    #if "catburger" in _proc_line or comicid[1] == "ga210214":
    #  print(_proc_line)

    writer.writerow([_proc_line, comicid[1]])
  return
  
output_to_file = "ga.csv"
w = open(output_to_file, "w", encoding="utf-8", newline='')

with open(old_file_name, 'r', encoding="windows-1252") as f:
  try:
    cleanup(f, w)
  finally:
    w.flush()
    w.close()
file_name = output_to_file
