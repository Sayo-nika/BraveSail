
label ca6:
    
    "It's early in the evening when we finally make it back to Sayonika's dorm."
    "I can feel my legs begin buckle under the weight of my own laziness as we enter."
    mc "I think I can feel my legs buckling under the weight of my own laziness."
    mc "So much walking today..."
    "I collapse onto a nearby beanbag chair, it's soft, pink fabric engulfing me as Sayonika looks on amusedly."
    sm "It wasn't even that long of a travel! You must be pretty out of shape, [player]."
    mc "I'm sorry - who ran out of breath this afternoon after a brisk walk from her house to the train station?"
    #Was it afternoon? Change if needed.
    #Swap the below line for the one above depending on if we're keeping Sayonika as an unfit small child or not lululul
    mc "Guilty as charged. I'll take sitting in a lawn chair with my feet kicked up and a glass of lemonade in my hand-over a brisk run any day."
    "Sayonika rolls her eyes as she plops down in an adjacent, similarly pink beanbag."
    "Description of the fancy not-Sayori house."
    sm "So what do you think of this place so far?"
    mc "The town? It's great!"
    mc "I actually had a lot of fun just going around exploring and reacquainting myself with everyone today. Thanks for that."
    #sm smile
    sm "No problem! That's good to hear!"
    sm "Besides, it wouldn't do to have a fellow literature club member-not knowing that all his favorite friends were here and what they were up to!"
    #sm surprised/"o" mouth
    mc "Hey, speaking of which, I haven't really heard all that much about you, aside from us going to the same highschool."
    mc "Tell me more about yourself. What've you been up to here?"
    #sm normal
    sm "Courier."
    mc "Mail delivery?"
    mc "You, of all people does mail delivery?"
    mc "I thought you were a coder."
    sm "Ehehe~."
    mc "So what do you like to do when you're not busy delivery mail?"
    sm "Funny you should ask that, [player]!"
    sm "I actually joined the literature club because I like writing, particularly poems."
    #sm blush
    sm "Not that they're by any means fantastic, but I don't think they're terrible."
    #sm normal
    sm "If you want, I can show you how to write some yourself. Maybe we can give eachother some inspiration!"
    #sm big smile
    sm "It can be part of our nightly bonding time!"
    #poem minigame
    sm "Hmmm..."
    sm "That doesn't look half-bad!"
    mc "It's been a while since I last wrote a poem, so I'll take that as a compliment."
    #line below feels awkward. Change it?
    "Come to think of it, the last time I wrote was back at the literature club."
    "Or-for it, at least. Now that I think about it, it seems a little strange that we never did any actual writing {i}during{\i} the club meetings."
    sm "So do you wanna see mine?"
    mc "I mean, it's only fair considering you helped me with this."
    #sm poem
    sm "Sooooo~? Whatcha' think?":
    # Can add a choice here if we wanna stick to the original DDLC theme of being able to say we liked a poem or not
    # (...we could do that in the original, right?), or we could ignore the second option and just go with the first
    # option of dialogue if we wanna keep it straight and choiceless, letting our poems in the future dictate whose
    # poems we like.
    menu:
        "I like it.":
        
            mc "I think it turned out good! You have some really good writing abilities."
            sm "Awww, thanks [player]! For the record, I think yours turned out pretty well, too!"
        
        "I don't like it.":
        
            mc "It's... okay."
            mc "Definitely not bad."
            #sm laugh
            sm "Haha, it's okay. I get it. I guess we just have different writing styles."
            sm "I actually thought the same about yours, too!"
            mc "Hey!"
            
            
    sm "So how'd you ever get involved with the literature club, [player]?"
    mc "Long story short, I sold my soul to a club fraught with embarassment and harassment for a single cupcake."
    mc "I have regretted this decision ever since."
    mc "How about you? Your sister* was in it, wasn't she?"
    #they're related right
    sm "Mmhmm! How about you?"
    mc "My childhood friend likes to sign me up for things without telling me."
    sm "*giggling* Yeah, Sayori seems like the type."
    # More conversation? Not sure if I should keep it short.
    mc "{i}*yawn*{\i}"
    mc "Y'know, I think I'm ready to hit the hay. Care to point me to my room?"
    "Sayonika points behind me to a white, wooden door standing right inside the beginning of the hallway."
    sm "Right down that hall, first door on the left."
    mc "Right. Thanks!"
    sm "No, left!"
    mc "..."
    mc "Ha. Ha."
    sm "Ehehe~"
    # slep/end CA6