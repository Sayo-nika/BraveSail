label ca4:
    stop music fadeout 1.0
    scene bg library_out
    with wipeleft
    "We arrive at something called... the library."
    "Still acting like a gentleman because apparently it’s what I do best, I gently open the door for Sayonika and enter."
    scene bg library_in
    with wipeleft
    "Well hey, The library looks just like, well... like a library!"
    "Lots of books, lots of tables, lots of bookshelves... I really can’t help but think about Yuri picking up an anatomy book and doing ‘you know what’... is that weird?"
    "We proceed to walk towards the main counter where I spy someone I recognize..."
    "It’s Yuri."
    play music t6
    show yuri 1 at t11
    y 3bn "S-Sayonika? What are you doing here? I thought you said you didn’t like reading in here..."
    show yuri at t21
    show sayonika 2b at f22
    sm "Ehehe... well..."
    sm 4e "I was just showing someone around the city, sooo I decided to come over with him to the library: my good friend [player]!"
    mc "More like acquaintance."
    sm 1i "Yeah... I suppose that’s a better way of putting it. We met each other earlier at the train station."
    sm 3b "He’s gonna stay with me for summer school."
    "Yuri appears to look at me, trying to confirm what she is hearing."
    show sayonika at t22
    mc "Yes, that’s right."
    show sayonika at f22
    sm 1r "Is there something wrong Yuri?"
    show yuri at f21
    show sayonika at t22
    y 3bp "A-Ah...!"
    y 4bb "Everything is fine... I just wasn’t expecting you here. The Portrait of Markov sucked me in again so I’m glad you came..."
    y 2ba "How may I help you?"
    show yuri at t21
    mc "Well, we were here to meet you."
    mc "Though the last place I’d expect you to be working in is a library."
    mc "So basically, Sayonika mentioned you’re going to summer school with us."
    show yuri at f21
    y 2bq "O-oh. She did?"
    y 2bj "Well... it’s true that I {i}am{/i} going to summer school as well..."
    y 3bn "Not because I failed this year’s classes...!"
    y 4bb "That would be awful for my mental health..."
    y 1bh "But because Monika made us come, what with that contract of hers..."
    show yuri at t21
    mc "Guess I was part of that contract too..."
    
    "That reminds me..."
    menu:
        "Snitch on Sayonika.":
            $ sayonika_snitch = 1
            jump sayonika_snitch_return

        "Stay quiet.":
            $ sayonika_snitch = 0
            mc "...it's nothing. So I was just thinking, Yuri. Do you get paid?"
            y "Yes, yes I do."
            mc "How much do they pay you?"
            y "I'd rather not say. It's a little embarrassing."
            mc "I understand."
            mc "Oh yeah, can I borrow a pen? I need to write down the times for the train..."
            y "P-pen...?"
            y "Ahah... I think you... m-meant pencil..."
            mc "....."
            mc "........."
            mc "What?!"
            "It takes me a few seconds to realize my mistake."
            mc "Oh shit, I'm sorry! I didn't realise you still don't like that word!"
            mc "I'm really sorry!"
            sm "[player]! Did you do that on purpose?!"
            mc "Look, I'm really sorry, okay?!"
            sm "Stupid!! You shouldn't do that! You're so evil!"
            
            mc "...well."
            menu:
                "Break the silence and snitch.":
                    $ sayonika_snitch = 2
                    mc "I wouldn't say I'm the evil one."
                    mc "In fact! I should say that you're the evil one here."
                    sm "Huh?! Oh, wait a minuteee! I mean you're just bonkers!... [i]he's not buying it, is he...?[/i]"
                    mc "Sorry, what was that? Oh yeah! I forgot to mention something, Yuri..."
                    jump sayonika_snitch_return

                "Let it go and move on.":
                    mc "...nevermind."
                    mc "I'm really sorry, Yuri. I won't do it again!"
                    $ sayonika_snitch = 0
                    pass
    
    label sayonika_snitch_return:
        mc "Sayonika made a {i}cutting{i} joke about you before we came."
        show yuri at f21
        y 3bp "S-Sayonika!"
        show sayonika at f22
        show yuri at t21
        sm 1p "[player]!!"
        show sayonika at t22
        "I shrug, because it's what she deserves."
        show yuri at f21
        y 2br "You know I hate those jokes, and they're really starting to get on my nerves..."
        show sayonika at f22
        show yuri at t21
        sm 2i "S-Sorry Yuri, I swear I’ll stop this time..."
        "Stop 'this time?'"
        show yuri at f21
        show sayonika at t22
        y 2br "This is the fifth time you’ve made one of those jokes..."
        y 2bt "You always say you’ll stop but you never do..."
        y 2br "How do I expect you to keep your word this time...?"
        show sayonika at f22
        show yuri at t21
        sm 1i "U-um... ehehe..."
        show yuri at f21
        show sayonika at t22
        y 1bw "Fine... I’ll forgive you one more time."
        y 1bg "If another one of those jokes comes out of your lips..."
        show sayonika 1x at h22
        y 2by7 "I won’t hesitate to shove some soap into your filthy, disgusting, putrid mouth."
        pass

    y 1be "Ahm... apart from that, what books should I get you two?"
    mc "I would like... hm..."
    y "Wait. I think I know of a book you two might like."
    "Yuri heads towards a bookshelf and returns with two books in her hands."
    y "[player], I know you don’t read a lot, so I thought this book might be kind of fitting for you."
    y "It’s a short read so it will be a little easier for you to read along."
    "I take a look at the book’s cover."
    "It reads \"Go the Fuck to Sleep\" by Adam Mansbach."
    mc "Thanks Yuri. This definitely looks like a must-read for my kind.."
    y "I’m glad."
    y "As for you, Sayonika..."
    y "You have to read this book about... PHP."
    sm "PHP?"
    y "It’s some programming language that I suppose fits you as a person so I thought why not give it a read."
    sm "Oh... uh, thank you, Yuri!"
    y "By the way, those are the books you will be reading this summer."
    mc "Guess I got the easy book to read then."
    sm "Wait, whaat? No fair! Why do I have to read a 500 page textbook about a coding language while [player] gets a little book with a short story about how he can go the heck to sleep?!"
    y "Sayonika! Shhh...!"
    y "This is a library! Please! Don’t you have any manners?"
    sm "Ehehe..."
    y "For goodness sake..."
    y "Come on, I’m sure you already know about how dense [player] is by now."
    mc "{i}I’m not dense! Hmph!{/i}"
    "I think I’m slowly turning into a tsundere."
    y "Sorry, I meant you’re not familiar with reading books. I remember when you told me that novel books are your mortal enemy because they lack pictures."
    y "What did you expect me to do? Give him a biography? Give him some geography?"
    y "He’s too new to read something without pictures to go along with the words."
    y "And he wouldn't possibly know how to answer the questions in Monika’s Summer Reading Test Papers if I gave him something different."
    "Are you calling me a child? Ow, my feelings..."
    "But this doesn’t explain why I have to read a textbook while he gets to read a short story!"

    if sayonika_snitch = 0:
        sm "Is it because you think I can read this?"
        y "If you can read books, then you can read that book on PHP!"
        sm "Okay, I understand. You want me to read this because I'm stupid and I need more brain."
        y "You've already nailed your first assignment from me on realising your stupidity. Good job~"
        sm "Meanieee!"
        mc "Come on, you two... Sayonika, we need to find Sayori now."
        sm "Oh yeaaah. I forgot!"
        mc "What did you forget?"
        sm "I forgot about Sayori, we still need to check on her!"
        mc "Now that I think about it... why exactly didn't you check beforehand?"
        sm "Um... I didn't think about that."
        mc "Hello; Sayonika's Brain? This is [player] asking you to think harder!"
        sm "Uwaaaa! I'm sorry!"
        mc "I'm kidding. Let's go, then!"
    if sayonika_snitch = 1 or 2:
        sm "Is this revenge for the joke I made?"
        y "What did you think? Did you think I gave it to you just because I thought you wanted to code? I already know you’re nothing like Monika!"
        y "So take a spoonful of my medicine and see how it feels!"
        sm "Oh... oh. Oh. W-well, now we need to find Sayori and make sure she’s going as well, even though I have a feeling everyone from the Literature Club is going, including me..."
        mc "Where could she be right now though?"
        y "I did see her come in here to run some errands, and then left. I think she was heading... south maybe?"
        mc "Well, I guess we should go and find her then!"
        
    "Hmmm..."
    menu:
        "Leave the Library quietly.":
            mc "See you later, Yuri."
            pass
            $ slap_sayonika = False
        "Slap Sayonika before leaving.":
            "I slap Sayonika so painfully that the noise can be audibly heard throughout the huge library."
            sm "Uwaaaaaaaah!!"
            mc "Alright. See you later Yuri."
            y "See you two later!"
            $ slap_sayonika = True

    scene bg library_out
    with wipeleft
    "We walk out of the library through the glass door entrance and wave Yuri goodbye before beginning to walk down the street."
    "We stop for a moment, so I decide to say something embarrassing to her to see how she’d react. As they say, it’s better to get to know the kind of person the girl you're going to be living with for the whole summer is."
    mc "Hey... Sayonika?"
    sm "What’s up [player]? {i}Uh oh...{/i}"
    mc "When we get back to your place tonight... "
    mc "Can you read me the book Yuri gave me when I go to bed?"
    sm "Uwaaa!!"
    sm "You have to be joking... right?"
    mc "Do I look like I’m joking?"
    sm "Eheh..."
    sm "Uhmm..."
    sm "I guess... I c-can...?"
    mc "Haha, success!"
    "I can’t believe she just agreed to read me Go the Fuck to Sleep tonight!"
    "Doing this will definitely help me find out more about who Sayonika is as a person."
    "But there’s no way I can stop now, there must be more I can do to improve this!"
    "I have to stretch the dough as far as it goes if I can, by showing her the book and telling her about how I’m about to ‘going the fuck to sleep’ so she can read me it."
    "I love it! It’s so devilish yet funny at the same time!"
    mc "Thanks Sayonika! You’re the greatest!"
    "This day just keeps on getting better and better~"
    return
