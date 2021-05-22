import re
import csv

def stripm(text):
  
  arr = text.splitlines()
  ret = ""
  
  for i in arr:
    ret = ret + i.strip() + "\n"
    
  ret = ret.strip()
  
  return ret

def _find_first_comicid(line, ln=None):
  
  try:
    
    # QUIRK: dataset has a spew of typos and oddities, so the regex has to be complex
    # [0] [0] full id [1] comic [2] nothing [3] sep
    result = re.findall(r'^((g[as]|dr|pg|)[0-9-]+)(\s|)([-.\* ]+)', line, flags=re.I)

    if len(result) <= 0:
      raise IndexError("No match for regex", result, line)
    if len(result[0]) <= 0:
      raise IndexError("No group in match 0 in regex (undefined behaviour)", result[0], line)

    return result[0]
  
  except Exception as e:
    
    raise IndexError("Can't find comicid for line number %s" % ln) from e

def cleanup(input_file, output):
  
  lines = input_file.readlines() # WARNING: this is bad, though this is fine yet
  writer = csv.writer(output)
  
  writer.writerow(["transcript", "comic"])

  _skip_ahead = 0

  for i in range(len(lines)):
    
    # skip-ahead
    if _skip_ahead >= 1:
      _skip_ahead = _skip_ahead - 1
      continue
    
    line = lines[i].strip()
    
    # find comicid (for merging lines together)
    comicid = _find_first_comicid(line, ln=i)
    
    _proc_line = ""
    
    # hack to merge lines to one
    for i2 in range(len(lines) - i):
      
      _loop_line = lines[i + i2].strip()
      if _loop_line == "-" * len(_loop_line) or _loop_line == "." * len(_loop_line):
        _skip_ahead += 1
        continue
      
      _sub_comicid = []
      try:
        _sub_comicid = _find_first_comicid(_loop_line, ln=i + i2)
      except: # line has no comicid header?
        _proc_line += " " + _loop_line
        _skip_ahead += 1
        continue
      
      if _sub_comicid[0] != comicid[0]:
        break
   
      if i2 == 0:
        _proc_line += "-"
      _proc_line += " "
      # hax
      _proc_line += _loop_line[len(comicid[0])+len(comicid[2])+len(comicid[3])-1:]
      
      if i2 > 0: # NTS: not skipped one line self
        _skip_ahead += 1
    
    # final processing
    # TODO: what if i commented this out?
    _proc_line = re.sub("(\s)+", r"\1", _proc_line)
    _proc_line = "\n- ".join(_proc_line.split("- "))
    _proc_line = stripm(_proc_line)

    writer.writerow([_proc_line, comicid[0]]) # NOTE: this accounts for gpt-2-simple, which reads [0] only for csvs
    
  return
