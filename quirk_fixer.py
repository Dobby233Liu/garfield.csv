"""
Fills the blank of the automagic with human fixups.
"""

# Lookup table to fix comicids
# Contains exact lines from the files.
# There are A LOT of these. enjoy free reading!
# line: (...comicid regex params, actual clip length)
comicids_fix = {
    # Dilbert
    "Why did you add this button the the user interface? You told me to. - Why would I tell you that` You always suggest random changes to create the illusion of adding value. - Well, remove that button. It's only on your copy.": ("070202", "", "", "", 0),
    "980626 -- Your performance was excellent, but there's no bonus this year - Why not? - The company lost a fortune in the Elbonian currency collapse. - But in a way, it's your own fault for working here. - Thanks. - That takes the sting out.": ("980826", "", " ", "--", -1),
    "051113 -- I must mark my territory by insisting on a change to the prototype. - Give it a wireless Internet option. It already has one. - What doesn't it have? An idiot designing it.": ("050113", "", " ", "--", -1),
    "081119 -- connections to hope.": ("080119", "", " ", "--", -1),
    "091022 -- around.": ("091020", "", " ", "--", -1),
    "130202 -- goes down.": ("130302", "", " ", "--", -1),
    "130203 -- Do you mind if I rummage through the trash in the technology lab? Um, okay. - I'm getting back to my hunter-gatherer roots. - SCORE! THESE OLD POWER CORDS SELL ON EBAY FOR UP TO $3 APIECE! - Ha ha! I'm a genius who turns trash into gold! -": ("130303", "", " ", "--", -1),
    "130203 -- How's that compare to whatever you're doing here? - Well, I'm removing valuable features from our product so we can... - ...gouge our customers with the---upgrade. - Wow. Your life is a total waste. Not if I sell the power cord.": ("130303", "", " ", "--", -1),
    
    # TODO
}

def find_first_comicid_quirkfix(text):
  fix = comicids_fix.get(text, None)
  return fix
