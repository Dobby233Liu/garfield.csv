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
    result = re.findall(r'^((g[as]|dr|pg|sh|)[0-9-a-zA-Z]+)(\s|)(--|- -|..|. .|\*\*|\* \*)', line, flags=re.I)
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
  _dquirk_done = False # resolve one qurik
  #_nameless_count = 0

  for i in range(len(lines)):
    
    if _skip_ahead >= 1:
      _skip_ahead = _skip_ahead - 1
      continue
    
    line = lines[i].strip()
    if (line == ("-" * len(line)) or line == ("." * len(line))):
      continue
    
    # find comicid (for merging lines together)
    comicid = ()
    #try:
    if not _dquirk_done and not ("--" in line) and (_find_first_comicid(lines[i-2].strip(), ln=i-2)[0] == "070201"):
      comicid = ("070202", "", " ", "--")
    else:
      comicid = _find_first_comicid(line, ln=i)
    _dquirk_done = True
    #except IndexError:# as e:
      #raise
      #print(e)
      #comicid = ["_nameless_%s" % _nameless_count, "", "", ""]
      #_nameless_count += 1
    
    _proc_line = ""
    
    # hack to merge lines to one
    for i2 in range(len(lines) - i):
      
      _loop_line = lines[i + i2].strip()
      if ((_loop_line == "-" * len(_loop_line)) or _loop_line == ("." * len(_loop_line))):
        _skip_ahead += 1
        continue

      _sub_comicid = _find_first_comicid(_loop_line, ln=i + i2)
      if comicid[0] != _sub_comicid[0]:
        break

      if i2 == 0:
        _proc_line += "-"
      _proc_line += _loop_line[len(_sub_comicid[0]+_sub_comicid[2]+_sub_comicid[3]):]

      if i2 > 0:
        _skip_ahead += 1

    _proc_line = re.sub("(\s)+", r"\1", _proc_line)
    _proc_line = "\n- ".join(_proc_line.split("- "))
    _proc_line = stripm(_proc_line)

    writer.writerow([_proc_line, comicid[0]]) # NOTE: this accounts for gpt-2-simple, which reads [0] only for csvs
    
  return
