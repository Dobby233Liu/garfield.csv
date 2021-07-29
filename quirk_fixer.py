"""
Defacto patching to the datasets.
Fills the blank of automatic stuff with human fixups.
"""

unlabeled_entries = {
    "Why did you add this button the the user interface? You told me to. - Why would I tell you that` You always suggest random changes to create the illusion of adding value. - Well, remove that button. It's only on your copy.": ("070202", "", "", "")
}

def find_first_comicid_quirkfix(text):
  fix = getattr(text, unlabeled_entries, None)
  return fix
