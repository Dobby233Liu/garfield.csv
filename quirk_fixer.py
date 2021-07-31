"""
Fills the blank of the automagic with human fixups.
Warning: Please make sure these texts are in UTF-8!!!
(The original texts are read in Latin-1)
"""

# Lookup table to fix comicids
# Contains exact lines from the files.
# There are A LOT of these. enjoy free reading!
# LINE FORMAT: "exact text of stripped line": (...(comicid regex params), int(actual clip length))
# That makes this a nightmare
comicids_fix = {
    # Dilbert
    "980626 -- Your performance was excellent, but there's no bonus this year - Why not? - The company lost a fortune in the Elbonian currency collapse. - But in a way, it's your own fault for working here. - Thanks. - That takes the sting out.": (
        "980826",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "051113 -- I must mark my territory by insisting on a change to the prototype. - Give it a wireless Internet option. It already has one. - What doesn't it have? An idiot designing it.": (
        "050113",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "Why did you add this button the the user interface? You told me to. - Why would I tell you that` You always suggest random changes to create the illusion of adding value. - Well, remove that button. It's only on your copy.": (
        "070202",
        "",
        "",
        "",
        "",
        0,
    ),
    "081119 -- connections to hope.": ("080119", "", " ", "--", " ", -1),
    "091022 -- around.": ("091020", "", " ", "--", " ", -1),
    "130202 -- goes down.": ("130302", "", " ", "--", " ", -1),
    "130203 -- Do you mind if I rummage through the trash in the technology lab? Um, okay. - I'm getting back to my hunter-gatherer roots. - SCORE! THESE OLD POWER CORDS SELL ON EBAY FOR UP TO $3 APIECE! - Ha ha! I'm a genius who turns trash into gold! -": (
        "130303",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "130203 -- How's that compare to whatever you're doing here? - Well, I'm removing valuable features from our product so we can... - ...gouge our customers with the---upgrade. - Wow. Your life is a total waste. Not if I sell the power cord.": (
        "130303",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "130204 -- Should we buy the maintenance plan or just take our chances? What do you prefer? - I prefer to punish you for the maintenance plan and going over budget. But I also don't mind firing you for not buying if we later need it. - Which one of us has": (
        "130304",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "130204 -- a better job?": ("130304", "", " ", "--", " ", -1),
    "160424 -- There's no reason to over-engineer it. I can respect that.": (
        "160624",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "180919 -- I fell in love with a chatbot. - We met on a plumbing supply website. - It started innocently. I had a few questions about faucets. - Next thing I knew, she was getting flirty. - Now we chat for hours every night. - That is the most pathetic": (
        "180819",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "180919 -- thing I have ever heard, you creepy loser. - - Does your chatbot have a sister?": (
        "180819",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "190110 -- don't see why the three of us need to go to lunch. - It's just the two of you. I'm busy tomorrow. - I hear you're a lot like me. Sadly, yes.": (
        "190210",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "190111 -- Dilbert, I want you to invent a device that can scrub 100% of the CO2 out of the air. - 100%??? That would kill every plant in the world. - Do you know what that would mean for humans? Does the answer involve salad?": (
        "190211",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "201120 -- We bought a start-up that makes autonomous drones armed with machine guns. - For use by the military? Good idea. I hadn't thought of that. - It's too dangerous for private use. You sound just like my neighbor when he still had a gazebo.": (
        "200120",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "201021 -- I object to your Twitter profile. It says.. - \"My tweets are smart and usefull, so obviously they do not represent my employer.\" - SMORPH! Now see what you did to Wally.": (
        "201221",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "201022 -- You are all required to complete a class in ethics. - Wouldn't that make us the only ethical organization in our industry and create a competitive disadvantage that leads to our demise? - Stop your worrying. The class is required, but I'm not": (
        "201222",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "201022 -- expecting any of it to stick.": (
        "201222",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    "210105 -- I got the Covid-19 vaccination, so I'm feeling safe. - I feel sorry for you unvaccinated people who are marinating in a toxic soup of deadly viruses. - Thank you for your concern. Neener-neener.": (
        "210205",
        "",
        " ",
        "--",
        " ",
        -1,
    ),
    # TODO - you can use search in the website
    # Dilbert (in Deutsch)
    # TODO - it's unoffical, gonna take me a while. only offical i18n is https://www.gocomics.com/dilbert-en-espanol
    # Drabble
    # TODO - needs some effort
    # Garfield
    # TODO - lasagna.cz good
}


def find_first_comicid_quirkfix(text):
    return comicids_fix.get(text, None)
