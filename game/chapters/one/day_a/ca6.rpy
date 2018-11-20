
label ca6:
    scene bg kitchen
    with wipeleft_scene
    play music t6
    #scene bg sayonikabedroom
    #with dissolve_scene_full
    "It's early in the evening when we finally make it back to Sayonika's dorm."
    "My legs ache in waves of pain like an unstable electric current surging through cables."
    mc "Oww..."
    mc "So much walking today..."
    "I collapse onto a nearby beanbag chair. Its soft, pink fabric engulfs my body as Sayonika looks on, amused."
    show sayonika 1q at t11 zorder 2
    sm "It wasn't even that long of a travel! You must be pretty out of shape, [player]."
    mc "How are you any better? You were looking for the train station for so long, I thought you died after I called you!"
    sm 1p "I-It’s not my fault your sister didn’t show me where to look for you on the map!!"
    show sayonika 1k at t11 zorder 2
    "Sayonika sighs heavily as she plops down in an adjacent, similarly pink beanbag."
    "Her house looks fluffy and definitely cutesy in a sense"
    sm 1h "So what do you think of this place so far?"
    mc "The town? Oh, pretty good if I do say so myself!"
    sm 1i "I was talking about my apartment..."
    mc "I don’t care about your apartment."
    sm 1p "Heey! At least say something nice about it, you big meanie!"
    mc "Okay, fineeee!"
    mc "Your apartment looks so hot I could burst."
    sm 1n ".....F"
    sm 5a "Thank you for the compliment~!"
    mc "Heh."
    sm 1g "So how'd you ever get involved with the literature club, [player]?"
    mc "Hey, wait a sec! I should be asking YOU the question here!"
    mc "But since you asked first..."
    mc "Long story short, I sold my soul for a cupcake."
    mc "How about you?"
    sm 1i "I don’t remember! It’s been a while and I’m too sleepy~!..."
    mc "{i}*yawn*{\i}"
    mc "Ugh...same, I think I'm ready to hit the hay...point me to my room, would ya?"
    "Sayonika points towards the staircase."
    sm 1a "Up the stairs, you’ll see the bed sign on the door when you get to the door."
    mc "Cool, thanks."
    scene bg bedroom
    with wipeleft_scene
    "I walk up the stairs sluggishly as I head to the bedroom."
    "I arrive at the door and walk in, getting into bed while taking my clothes off."
    if read_sayonika == True:
        "Then out of the blue, I remember what Sayonika said she’d do. I mean sure, it wasn’t a promise, but avoiding it would be a sign of untrustworthiness... "
        mc "SAYOOONIKAAAA!! YOU HAVE TO READ ME THAT BOOK YOU SAID YOU’D REEAD!"
        sm "DO I HAAAAVE TO?!!"
        mc "YEEESSS! YOU MUUST!!"
        "A few clangs and bangs later, Sayonika starts walking to the bedroom to read me a bedtime story. One that I may not ever forget!"
        show sayonika 1y at t11 zorder 2
        sm "I’m here with your silly book now..."
        mc "I want you to read it like a little girl."
        show sayonika 1u at h11 zorder 2
        sm "Whaaaaa?!"
        mc "Oh come on, do it...! Please?"
        "Sayonika’s face turns red with embarrassment."
        sm 1i "F-Fine… just… just this once…!"
        "And so she began reading it."
    scene black
    with dissolve_scene_full
    "{i}Hi, welcome to the end of November Preview. We’re starting to progress quicker however we had a slowdown over the month. Sorry for the wait and this mod will be completed by December if all goes well!{/i}"
    "{i}~ Sayonika VN Team/n/nWell... those that are actually active and helping us out...{/i}"
return