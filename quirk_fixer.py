"""
Fills the blank of the automagic with human fixups.
"""

# Lookup table to fix comicids
# Contains exact lines from the files
# line: (...comicid regex params, actual clip length)
comicids_fix = {
    # Dilbert
    "Why did you add this button the the user interface? You told me to. - Why would I tell you that` You always suggest random changes to create the illusion of adding value. - Well, remove that button. It's only on your copy.": ("070202", "", "", "", 0),
    "980626 -- Your performance was excellent, but there's no bonus this year - Why not? - The company lost a fortune in the Elbonian currency collapse. - But in a way, it's your own fault for working here. - Thanks. - That takes the sting out.": ("980826", "", " ", "--", -1),
    "051113 -- I must mark my territory by insisting on a change to the prototype. - Give it a wireless Internet option. It already has one. - What doesn't it have? An idiot designing it.": ("050113", "", " ", "--", -1),
    # TODO
}

def find_first_comicid_quirkfix(text):
  fix = comicids_fix.get(text, None)
  return fix
