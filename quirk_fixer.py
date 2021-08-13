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
    # TODO - it's unoffical, gonna take me a while
    # Drabble
    # TODO - needs some effort; search on GoComics
    # Garfield
    "ga810102 -- Just what is a diet? - A diet is self-denial. - Fortunately, I'm such a swell fellow I haven't the heart to deny myself anything.": (
        "ga820102",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga830216 -- Rather than fix your breakfast every day, Garfield, I've decided to let you serve yourself. - - Maybe that wasn't such a good idea.": (
        "ga820216",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga860610 -- zzzzzzzz - Hey, Garfield, when was the last time you saw my pet frog, Herbie? zzzzz - SNAK! At lunch.": (
        "ga830610",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga900921 -- Here you goo, Pooky. - Hang on tight, now. - Sniff, they grow up so fast.": (
        "ga900221",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga900922 -- Wanna go jogging? I'm busy. - Honestly, Garfield. I have the feeling you think more of that teddy bear than you do of me! - Pay no attention to ol' what's-his-name, Pookie.": (
        "ga900222",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga900923 -- - - Gave your bear a bath? How'd you guess?": (
        "ga900223",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga900924 -- Why is that teddy bear of mine always getting lost? Why can't I ever find him? - POOOOOOOO-KY! - And why am I cupping my hands over my mouth?": (
        "ga900224",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga900928 -- Stop, Vermin. Eek. - You'll never escape. Help, help. - One of the great chase scenes. Z z": (
        "ga900228",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga910125 -- Did you know that pets are good for exercise? - BURP -": (
        "ga920125",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga930523 -- BANZAI! - SPLOOSH! - Why didn't you warn me we were having soup?": (
        "ga920523",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga980311 -- I owe Odie an apology. - PUSH CRASH! - Now I owe him two.": (
        "ga980331",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga001112 -- Dinner's running late. - Fine. - Any last words?": (
        "ga011112",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga100130 -- Garfield, this is my life. - Cleaning up cat hair. - How sad is that? Now, about my litter box...": (
        "ga140130",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga150203 -- My new year's resolution is to lose weight. - You? Lose WEIGHT?! Yeah... - I'm gettin' a real fly gut.": (
        "ga150103",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga130505 -- I like to think of myself as smart. - Good for you. - I like to think of myself as skinny.": (
        "ga150305",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga150416 -- - - WOOOOOOO! - Air guitar - - BURP - Air lasagna.": (
        "ga150426",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga150314 -- You should watch less television. - Okay. - What channel is that on?": (
        "ga150514",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga150604 -- every sunday.":("ga150614","ga"," ","--"," ",-1),
    "ga130306 -- - - FLAP FLAP FLAP FLAP FLAP - LAP FLAP FLAP FLAP FLAP FL - LAPFLAPFLAPFLAPFLAPFLAPFL - PFLAPFLAPFLAPFLAPFLAPFLAP - What's it like out there? March.":(
        "ga160306",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga160505 -- I demand my rights! - - With chocolate syrup!":(
        "ga160405",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga150611 -- Don't tell Odie, but sometimes I enjoy being around the little fella. - - Me and my big thought balloon...":(
        "ga160511",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga160627 -- - Time marches on. - That would not have been my guess.":(
        "ga160727",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga161120 -- What did you get Garfield, for Christmas, Jon? - I got him a c-a-t t-o-y. - He's right here. I WANTED a j-e-t s-k-i, you d-o-r-k.":(
        "ga161220",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga170202 -- Let's see...should I get Odie a squeaky bone or a dingle ball? - What the heck, it's chistmas...I'll get him both! - And what would YOU like? To slap you silly.":(
        "ga171202",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga170203 -- - - - - - - Our giant inflatable Rudolph blew over again.":(
        "ga171203",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga180313 -- - Here you go, Garfield. - Still warm from the dryer.":(
        "ga180213",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga150819 -- I'm eating healthier these days. - - Sorry, I can't say that with a straight face!":(
        "ga180519",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga130313 -- "Dear Ask A Dog, the pleasure of your company is requested for a dinner party.. - Can we expect you at six o'clock?\" - \"Signed, Mr. and Mrs. Frederick J. Flea\".":(
        "ga190313",
        "ga",
        " ", "--", " ",
        -1
    ),
    "ga190727 -- We should think of something to do. - And then NOT do it. - How is that different from any other date? The thinking!":(
        "ga190927",
        "ga",
        " ", "--", " ",
        -1
    ),
    # TODO - search on lasagna.cz or GoComics
}


def find_first_comicid_quirkfix(text):
    return comicids_fix.get(text, None)
