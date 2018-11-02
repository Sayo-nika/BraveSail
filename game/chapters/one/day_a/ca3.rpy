label ca3:
    # TODO: Replace this with bakery background
    stop music fadeout 0.5
    scene bg bakery_midday
    with wipeleft
    play music t3
    "We sprint all the way to a bakery."
    "I decide not to ask questions as to why we ran all the way to something so insignificant."
    sm "W...w...we’re...here..."
    mc "Dang...! you must be...complete-*cough*-completely drained...!"
    sm "Y...you...think so...? W-well...I can...run a few...more laps...!"
    mc "Sorry...did you...say something? I...think it...*cough* involved try...trying to exercise...to death...?"
    "Before Sayonika could give a response, the doors to the bakery swing open and a friendly face greets us."
    n 1bk "Woah! Is that really you, [player]?"
    mc "Still...the same...narcissist I was...back then..."
    n 5bi "So you're still a big dummy! Hmph."
    n "Well, you two better get inside and catch your breaths before we talk to each other, I don’t wanna burn you guys out!"
    "We walk inside slowly, breathing heavily."
    #new scene, to the bakery
    BG: Inside Bakery (Mid-day)
    "A few moments pass before I finally catch my breath. I notice the walls lined with croissants, cinnamon buns, apple pies and more. A paradise..."
    "MADE IN HEAVEN"
    mc "Woah...this place...it smells like pure sugar!"
    n 1bl "We have all of the baking goods you’ll ever need!"
    mc "But do you have...banana pie?"
    n 1bz "Yep! We have banana, strawberry, cranberry, apple, gooseberry, orange, blueberry, blackberry, plum, grape, chocolate, vanilla, ice cream, ham, chicken, vegetarian…"
    mc "I’m gonna stop you right there."
    sm "See, [player]? This is why I brought you here~"
    mc "You probably just came here to get free food from Natsuki."
    n 1bk "She always does it, so I’ve just made it a daily habit."
    n 1bt "Eventually I’m just gonna put a free sample outside for Sayonika to eat..."
    sm "Ehehe..."
    sm "I just love this place! The food is so good!"
    n 5bh "Come on...it’s nothing but an average, ordinary bakery...sheesh."
    "Sayonika began lecturing Natsuki about how her food is always amazing and how she puts high standards into each and every piece of food she makes."
    n 12bc "Okay, okay! Stop it, you big baka!"
    sm "Say it! Tell me that your food is the best, that it’s one of a kind!"
    n "Okay, okay! Jeez..."
    n 2bk "Oh, [player]. I forgot to ask you."
    n "What are you doing here in—"
    "Before Natsuki can finish her sentence, a redhead walks in shouting at her."
    #show mio, hide name
    mi 8q "Come on, Natsuki! Did you forget the order for the huge pack of flour already?!"
    n 2bh "Just give me a second, Mio..."
    #change name to Mio
    mi 8t "I already gave you 5 minutes!"
    n 2bf "Listen here, my friends have come to say hello, so if you don't get your butt over to the truck and unload it without me, I'll fire you on the spot! Understood?!"
    mi 8u "YES, MADAM!" #Natsuki is not a Guy! Edited because cringe
    show mio at thide
    hide mio
    "Mio marches through the backdoors before Natsuki continues."
    n 5bi "Sorry about that. She's a nuisance."
    n 2bk "Sorry, as I was saying, what are you doing here?"
    mc "Summer-school."
    n 5bl "Say what?"
    mc "You know, school. In the summer."
    "Natsuki starts to snigger and chuckle before heading into a laughing fit."
    mc "Here, I'll do you one better – Sayonika's my roommate too."
    n 5bt "Did you both really – pff... – both of you fell for Monika's bait?! Bahahaaaaa!!"
    n "It was...phaaahaa! It was right there, you just had to read between the lines!! Wait – although..."
    "Natsuki's tone changes immediately as soon as she suddenly stops laughing."
    n 2bk "Although that dirty devil probably learned a thing or two from school..."
    mc "Why exactly did she fool us and send us to a summer-school?"
    n 5bh "Well, 'cause she knows you're not gonna go if you're told there's a town festival you need to attend."
    n 5bs "Hell, I don't wanna go either but I have to manage the food and catering for everyone there."
    n "She knew I'd be forced to go, so she told me the truth straight away."
    sm "I can't believe we've been lied to!"
    mc "Can we talk our way out of this? I'm really not in the mood for a festival this summer."
    mc "Also, how'd Monika get my sister involved?"
    n 1bc "She's a sly fox, she'll manipulate anyone she comes across that she needs."
    sm "I don't like her much too...she's so...depressing!"
    mc "Yeah, tell me about it. She's the definition of a depression pill condensed into human flesh."
    n "Well, now you know what it is and that I'm going..."
    n "However, you should find out who else is going to the supposed summer-school."
    mc "I can try but I won't promise anything."
    sm "It's OK, [player]! I know where the rest of the gang is!"
    mc "Sure, lead the way."
    n 2bl "Looks like you two are getting along well! I guess I'll see you guys later!"
    mc "Totally."
    
    scene bg plaza_day
    with wipeleft
    hide natsuki
    "We wave our goodbyes before Sayonika grabs my shirt, pulling me to our next destination."
    mc "Hey, let go!!"
    sm "Oops! Sorry, ehehe..."
    mc "Where are you taking me?"
    sm "Someone who's on the {i}cutting edge{/i} of technology."
    "I suddenly realise what she means."
    mc "Oh, come on!! Seriously?!"
    sm "Whaat? It was a good joke!"
    mc "Bad joke! No encore, no encore!!"
    #where ‘Sayonika's stupid joke’ is, create a special font type/definition for it to signify it being a keyword.
    "{i}I should tell Yuri about Sayonika's stupid joke...{/i}"
    return
