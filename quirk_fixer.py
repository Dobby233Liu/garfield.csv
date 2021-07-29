"""
Fills the blank of the automagic with human fixups.
"""

# Lookup table to fix comicids
comicids_fix = {
    "Why did you add this button the the user interface? You told me to. - Why would I tell you that` You always suggest random changes to create the illusion of adding value. - Well, remove that button. It's only on your copy.": ("070202", "", "", "")
}

def find_first_comicid_quirkfix(text):
  fix = getattr(comicids_fix, text, None)
  return fix
