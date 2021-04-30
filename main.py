import re
import csv

def stripm(text):
  
  arr = text.splitlines()
  ret = ""
  for i in arr:
    
    ret = ret + i.strip() + "\n"
    
  _ = _.strip()
  
  return _

# TODO: account for dlibert
def _find_first_comicid(line, ln=None):
  
  try:
    
    # QUIRK: dataset has a spew of typos, so the regex has to be complex
    result = re.findall(r'^(\s|)((g[as]\w+)(\s|)(--|\.\.))', line)
    if len(result) <= 0:
      raise IndexError("No match for regex", result, line)
    if len(result[0]) <= 0:
      raise IndexError("No group in match 0 in regex (undefined behaviour)", result[0], line)

    return result[0][1:]
  
  except Exception as e:
    
    raise IndexError("Can't find comicid for line number %s" % ln) from e

def cleanup(input_file, output):
  
  lines = input_file.readlines() # WARNING: this is bad, though this is fine yet
  writer = csv.writer(output)

  _skip_ahead = 0

  for i in range(len(lines)):
    
    # skip-ahead
    if _skip_ahead >= 1:
      _skip_ahead = _skip_ahead - 1
      continue
    
    # find comicid (for merging lines together)
    comicid = _find_first_comicid(lines[i], ln=i)
    
    _proc_line = ""
    
    # hack to merge lines to one
    for i2 in range(len(lines) - i):
      
      _loop_line = lines[i + i2].strip()
      _sub_comicid = []
      
      try:
        _sub_comicid = _find_first_comicid(_loop_line, ln=i + i2)
      except: # line has no comicid header? TODO: that even happens???
        _proc_line += " " + _loop_line
        _skip_ahead += 1
        continue
      
      if _sub_comicid[1] != comicid[1]:
        break
   
      if i2 == 0: # NTS: why did i do this?
        _proc_line += "-"
      _proc_line += _loop_line[len(comicid[0]):]
      
      if i2 > 0: # NTS: not skipped one line self
        _skip_ahead += 1
    
    # final processing
    # TODO: what if i commented this out?
    _proc_line = re.sub("(\s)+", r"\1", _proc_line)
    _proc_line = "\n- ".join(_proc_line.split("- "))
    _proc_line = stripm(_proc_line)

    writer.writerow([_proc_line, comicid[1]]) # NOTE: this accounts for gpt-2-simple, which reads [0] only for csvs
    
  return
  
if __name__ == "__main__":
  # TODO: write a actual cli
  import sys
  fn = sys.argv[2]
  datname = sys.argv[1]
  with sys.stdout if fn == "-" else open(fn, "w", encoding="utf-8", newline='') as w:
    # QUIRK: why the fuck it has this encoding???
    with sys.stdin if datname == "-" else open(datname, 'r', encoding="windows-1252") as f:
      cleanup(f, w)
