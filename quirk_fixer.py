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
    '201021 -- I object to your Twitter profile. It says.. - "My tweets are smart and usefull, so obviously they do not represent my employer." - SMORPH! Now see what you did to Wally.': (
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

    "dr010201 -- Time to check the local traffic conditions... - Tipster No-Neck called to report a Rottweiler running loose along the northbound 710! - ...and now we've just received a call from tipster Drabble CORRECTING tipster No-Neck: It's not a":(
        "dr010301",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010201 -- Rottweiler, it's a DOBERMAN. -":(
        "dr010301",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010202 -- Let's go out to the freeways once again for a look at traffic... - Tipster Drabble reports that tipster NO-Neck just made an illegal lane change on the westbound 134! - And now tipster No-Neck reports that tipster Drabble is driving a vehicle":(
        "dr010302",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010202 -- with expired license tabs! - RRRRRRRRRR It's getting ugly out there, folks!":(
        "dr010302",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010203 -- Hi, Wendy! - Hello, Norman. - Get dressed in the dark, again? - Wow, how do you always KNOW these things??":(
        "dr010303",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010204 -- Wally and I are going jogging, honeybunch! JOGGING?? skattle skattle skattle - I've decided it's time to get in shape, so today I'm going to start jogging! Are you sure you can do it? - Of course I can do it! I'm going to start gradually, and":(
        "dr010304",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010204 -- increase my distance each day! - Come on, Wally! 'bye, boys! skattle skattle - - Forget something? No, that's far enough for today! Tomorrow we'll try to make it to the end of the driveway.":(
        "dr010304",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr011126 -- poem about me! Quiet! I'm on a roll!":(
        "dr011026",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr011127 -- - - - That's the worst mummy outfit I've ever seen! My costumer got dizzy!":(
        "dr011027",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr011128 -- I just love looking at the colors of autumn... - The reds, the yellows, the browns, the oranges... - The blues... The BLUES? - Blue isn't a color of autumn! - There's blue on that bag of Snickers bars! Oh, THOSE colors of autumn!":(
        "dr011028",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr011228 -- Welcome to Galtburger! May I take your order, please? - Hey, it's me. Oh, hi, Ralph! How ya' doin' ? - Do you want your usual, today? Yeah. - When you suddenly realize you've developed a close relationship with the drive-thru clerk, it's":(
        "dr001228",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr011228 -- probably time to have your cholesterol checked! So, how's the family?":(
        "dr001228",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr011229 -- Hey, Ralph! Hey. - Your usual jumbo chili cheese bacon burger with fries and a shake? - AHHEM!! COFF COFF (wife's in the car!) COUGH COUGH! - Uh, I mean, your usual garden salad and diet cola? So, how's your diet going, Ralph?":(
        "dr001229",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr011230 -- Well, the new millennium begins on Monday! - Again?? - It seems like we started a new millennium just last year! - Time really flies when you get to be my age!":(
        "dr001230",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr011231 -- Oh, this is an outrage! - The home owners association is demanding the immediate removal of my holiday decorations! - It's not even JANUARY FIRST, for cryin' out loud! - What's so bad about leaving Christmas decorations up until new year's":(
        "dr001231",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr011231 -- day?? - Maybe they were talking about your HALLOWEEN decorations!":(
        "dr001231",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010913 -- Boy, this is the life, Ralph! - Too bad you've been  such a creep over the years, or I'd invite you in for a dip! - Creep???! Who's the guy who picked up your newspaper every day when you were on vacation? You. - You also pick up my newspaper":(
        "dr020913",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010913 -- every day when I'm NOT on vacation! Yeah, but I usually put most of it back!":(
        "dr020913",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010914 -- You shouldn't stare into Mr. Steinbauer's back yard, dad. It's not polite! I don't care. - I'm going to start at his new pool until he invites me over to go swimming. - Eventually, my sad and forlorn look will make him feel guilty! SPLOOSH! -":(
        "dr020914",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010914 -- I don't think it's working. Nice cannonball!":(
        "dr020914",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr010915 -- That'll be one dollar. All I have is a $20 bill. - - - - KA-CHING! - Nineteen dollars is your change. - ...17, 18, 19. What's the matter? Don't you trust me?":(
        "dr020915",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr030301 -- No-Neck and I are going to the parade! Will we see you on TV? - No, the TV cameras are at the beginning of the five-mile parade route, when all the marchers are fresh. - We like to stand near the END of the parade route, when the marchers are":(
        "dr030101",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr030301 -- completely exhausted! Why? - We like to see their expressions when we hold up our sign! Half-Way Point":(
        "dr030101",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr030302 -- - Oh, yeah. I see it. - Very becoming, son! - See? I did SO grow a goatee!":(
        "dr030102",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr030303 -- I hate unloading the car after mom shops at BULK CLUB! I think it would be simpler if we just MOVED to Bulk Club! - Oh, hush! I save money buying in bulk! Where should I put the box of four dozen glue sticks?":(
        "dr030103",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr030304 -- - - I told you your untied shoelaces were an accident waiting ho happen! Shut up ant turn off the ceiling fan!":(
        "dr030104",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr030305 -- - FORE! - TOK! Good shot!":(
        "dr030105",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr060221 -- Boys, you've been watching TV all afternoon! - Here are a couple of books... - If you hear your mom come home, turn off the TV and act like you're reading 'em! - Keeping your kids out of trouble is part of a father's duty!":(
        "dr020621",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr060222 -- Poor Bob! He always has that dazed and confused look on his face. - Like he doesn't know who he is or what to do next! - Kind of like dad on a Saturday! ...and then, after you fix the garbage disposal, the trees need trimming. After that you":(
        "dr020622",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr060222 -- need to paint the patio furniture and clean out the garage...":(
        "dr020622",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr060223 -- Hi, Ralph! - - How are you? - - You wouldn't be eating something on the new sofa, would you? Especially after I warned you never to do that! - RALPH DRABBLE, OPEN YOUR MOUTH THIS INSTANT!! - Nothing! - You are SO not funny! I just like to":(
        "dr020623",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr060223 -- freak her out sometimes!":(
        "dr020623",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr060331 -- huh!":(
        "dr060131",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr071025 -- SCOOP SCOOP! - Hmmm... - Honeybunch, is it OK if I just polish off the rest of the carton? I suppose. Sweet!":(
        "dr070125",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr071026 -- - - - - CLOMP! skattle skattle skattle skattle Wally loves plastic water bottles!":(
        "dr070126",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr071027 -- That'll be $5.75 at the first window! OK - Pay Window Here's your change. Next window please! OK - Pick-Up Window Here's your order. Next. window, please. OK - Correction Window You got my order wrong AGAIN! ...sigh...":(
        "dr070127",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr071028 -- The following program contains graphic material, adult themes, mature situations, crude humor, explicit dialogue, nudity and violence. - Viewer discretion is adviced. I say OK! Me too! - Why can't we watch that show?? Because, in this house,":(
        "dr070128",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr071028 -- viewer discretion loses out to mother-of-viewer discretion!":(
        "dr070128",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr080328 -- Why are you swimming in my water dish? Ducks like water. - Can't you find someplace else to swim? - Sorry. It's the only place available. - Someone left the lid down on the porcelain pond again!":(
        "dr080228",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr080329 -- Today is February 29th, Penny! It's leap year day! I know. It's not fair! - Why does it have to be in FEBRUARY?? - Why can't they put the extra day in summer vacation or spring break? - I never thought of that! Better yet, they could squeeze":(
        "dr080229",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr080329 -- it in between Saturday and sundae!":(
        "dr080229",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr080513 -- Dad, LOOK!! - There's a SNAKE on our neighbor's roof! - Relax, it's fake. Our neighbor put it up there himself! - How come?? To scare away varmints, and keep birds from building nests on the house. - Some people put rubber snakes on top of":(
        "dr080413",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr080513 -- their houses, some people use fake owls...it has to be something scary enough to frighten critters away! - Maybe you should put something scary on OUR roof! I already did! - Hey! What happened to the picture of my mother?":(
        "dr080413",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr081228 -- Well, it's that time of year again. - First, the holidays are upon us... - - Then the holiday BILLS are upon us!":(
        "dr071228",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr081229 -- Welcome back to love songs on the radio! This song is dedicated to Bruce from Debbie! - Bruce, Debbie wants you to know how deeply she cares for you. She thinks about you night and day! - Her only desire is to spend every waking moment with":(
        "dr071229",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr081229 -- you for ever and ever! Sniff! - HEAD FOR THE HILLS, BRUCE!!":(
        "dr071229",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr081230 -- - - - - - - - Looks like the Christmas bills have started to arrive! At least his hair is getting exercise!":(
        "dr071230",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090330 -- When I was a kid, my dad made sure that his family always sat together at the dinner table and communicated! - Now that I'M a father, my family sits together and communicates, too. - Unfortunately, just not with each other! *chirp* text text":(
        "dr080330",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090330 -- press *chirp* press press text text *chirp* *chirp* text text press press":(
        "dr080330",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090424 -- Let's see...I need to check the calendar... - What the heck?? - Honeybunch, why is last year's calendar hanging on the wall? - Because the pictures are much prettier than this year's calendar!":(
        "dr080424",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090504 -- She'll have the chicken sandwich, and I'll have a cheeseburger! - FWEET! - That is the 1,000th cheeseburger you've ordered from our restaurant, Mr. Drabble! - You are now a member of our loyal customer hall of fame! - On behalf of everyone":(
        "dr080504",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090504 -- here at Down-N-Out Burgers, thank you and congratulations! - That was a little embarrassing! The ceremony over at the taco shop was much more dignified!":(
        "dr080504",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090520 -- Tonight's recipient of the lifetime achievement award is the man who actually coined the term \"Mall Cop.\" - Before that, we were just known as \"indoor retail security personnel\", which wasn't as catchy! - None of us would be able to call":(
        "dr080520",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090520 -- ourselves \"mall cops\" today, if not for this man! - Why are you crying? I never realized how GREAT I was!":(
        "dr080520",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090521 -- Hi, mom! Hi, dad! Norm, you're just in time to see me receive the lifetime achievement award! - Isn't that what they give to old people when their career is over? What?? - Yeah, they give somebody a lifetime achievement award, and then they":(
        "dr080521",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090521 -- don't feel so bad about getting rid of them! - Ralph, you look sick! Maybe he ate too many cocktail weenies!":(
        "dr080521",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090522 -- I'm getting out of here, honeybunch! WHAT?? - Norman just pointed out that they only give lifetime achievement awards to people whose careers are over! I'm too young for this!! - And the winner is RALPH DRABBLE! Where are you, Ralph? - Ralph?":(
        "dr080522",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090522 -- Come out from under this table! No!":(
        "dr080522",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090523 -- Ralph! Come back!! - We need to give you your award! Stop him!! - OOF! HEY! OUCH! LET ME GO!! - Good work, men! No problem! Ralph is pretty easy to outrun!":(
        "dr080523",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090524 -- I don't WANT a lifetime award! I'm too young!! But, Ralph! Look at all you've contributed... - The holiday spirit violation, mall bowling, mall golf, the mall cop olympics, the junior mall scouts... - You're just giving me a lifetime":(
        "dr080524",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090524 -- achievement award because you intend to phase me out!! - That's not true! We're giving it to you instead of a raise! Oh, OK then!":(
        "dr080524",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr090525 -- I love to watch the Extreme Home Makeover show! It's so heartwarming! - Sniff! - SOB - HONK - - - Why can't I watch my favorite show without everybody staring at me?!! - Because OUR favorite show is watching you watch YOUR favorite show!":(
        "dr080525",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
    "dr091125 -- 'bye grandma! Thanks again for dinner! - How did you like the turkey, Ralph? - cough cough cough! - I think it was undercooked!":(
        "dr051125",
        "dr",
        " ",
        "--",
        " ",
        -1,
    ),
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
        " ",
        "--",
        " ",
        -1,
    ),
    "ga860610 -- zzzzzzzz - Hey, Garfield, when was the last time you saw my pet frog, Herbie? zzzzz - SNAK! At lunch.": (
        "ga830610",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga900921 -- Here you goo, Pooky. - Hang on tight, now. - Sniff, they grow up so fast.": (
        "ga900221",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga900922 -- Wanna go jogging? I'm busy. - Honestly, Garfield. I have the feeling you think more of that teddy bear than you do of me! - Pay no attention to ol' what's-his-name, Pookie.": (
        "ga900222",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga900923 -- - - Gave your bear a bath? How'd you guess?": (
        "ga900223",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga900924 -- Why is that teddy bear of mine always getting lost? Why can't I ever find him? - POOOOOOOO-KY! - And why am I cupping my hands over my mouth?": (
        "ga900224",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga900928 -- Stop, Vermin. Eek. - You'll never escape. Help, help. - One of the great chase scenes. Z z": (
        "ga900228",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga910125 -- Did you know that pets are good for exercise? - BURP -": (
        "ga920125",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga930523 -- BANZAI! - SPLOOSH! - Why didn't you warn me we were having soup?": (
        "ga920523",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga980311 -- I owe Odie an apology. - PUSH CRASH! - Now I owe him two.": (
        "ga980331",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga001112 -- Dinner's running late. - Fine. - Any last words?": (
        "ga011112",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga100130 -- Garfield, this is my life. - Cleaning up cat hair. - How sad is that? Now, about my litter box...": (
        "ga140130",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga150203 -- My new year's resolution is to lose weight. - You? Lose WEIGHT?! Yeah... - I'm gettin' a real fly gut.": (
        "ga150103",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga130505 -- I like to think of myself as smart. - Good for you. - I like to think of myself as skinny.": (
        "ga150305",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga150416 -- - - WOOOOOOO! - Air guitar - - BURP - Air lasagna.": (
        "ga150426",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga150314 -- You should watch less television. - Okay. - What channel is that on?": (
        "ga150514",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga150604 -- every sunday.": ("ga150614", "ga", " ", "--", " ", -1),
    "ga130306 -- - - FLAP FLAP FLAP FLAP FLAP - LAP FLAP FLAP FLAP FLAP FL - LAPFLAPFLAPFLAPFLAPFLAPFL - PFLAPFLAPFLAPFLAPFLAPFLAP - What's it like out there? March.": (
        "ga160306",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga160505 -- I demand my rights! - - With chocolate syrup!": (
        "ga160405",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga150611 -- Don't tell Odie, but sometimes I enjoy being around the little fella. - - Me and my big thought balloon...": (
        "ga160511",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga160627 -- - Time marches on. - That would not have been my guess.": (
        "ga160727",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga161120 -- What did you get Garfield, for Christmas, Jon? - I got him a c-a-t t-o-y. - He's right here. I WANTED a j-e-t s-k-i, you d-o-r-k.": (
        "ga161220",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga170202 -- Let's see...should I get Odie a squeaky bone or a dingle ball? - What the heck, it's chistmas...I'll get him both! - And what would YOU like? To slap you silly.": (
        "ga171202",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga170203 -- - - - - - - Our giant inflatable Rudolph blew over again.": (
        "ga171203",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga180313 -- - Here you go, Garfield. - Still warm from the dryer.": (
        "ga180213",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga150819 -- I'm eating healthier these days. - - Sorry, I can't say that with a straight face!": (
        "ga180519",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    'ga130313 -- "Dear Ask A Dog, the pleasure of your company is requested for a dinner party.. - Can we expect you at six o\'clock?" - "Signed, Mr. and Mrs. Frederick J. Flea".': (
        "ga190313",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    "ga190727 -- We should think of something to do. - And then NOT do it. - How is that different from any other date? The thinking!": (
        "ga190927",
        "ga",
        " ",
        "--",
        " ",
        -1,
    ),
    # TODO - search on lasagna.cz or GoComics
}


def find_first_comicid_quirkfix(text):
    return comicids_fix.get(text, None)
