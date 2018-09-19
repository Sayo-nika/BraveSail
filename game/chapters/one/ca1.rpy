label ca1:
    stop music fadeout 1.0
    scene bg train_station
    with dissolve_scene_full
    play music t2
    "So here I am, waiting…"
    "Waiting…"
    "Waiting…"
    "The horizon looks nice - but I’m still unphased, with me being a couch potato and all."
    "That’s probably why I believe fate decided to take a dump in my sister’s mouth and have her sending me somewhere for the rest of the summer break."
    "And that means also means I have no manga or anime to watch until summer school is over."
    "Oh well… this is gonna be {i}fun…{/i}"
    "The train stops, marking the end of my journey and my window-gazing. Well... at the very least for now."
    "Nonetheless, I stand up carrying my things and walk outside of the train onto the station platform."
    "And so, the suffering begins."
    return

label ca2:
    scene bg plaza_day
    with wipeleft
    "After leaving the station, I sit down on a nearby bench before proceeding to call a number my sister handed to me before I left. She’ll take me to where I need to go, she said."
    "I sigh and call the number."
    mc "Hello?"
    "I didn’t expect she’d answer over my greeting."
    $ sm_name = "???"
    sm "Hello? Who is this?"
    mc "Uhm… It’s me, [player]... my sister told me you knew each other… and{nw}"
    $ _history_list[-1].what = "Uhm… It’s me, [player]... my sister told me you knew each other… and—"
    "She gasps and squeals in the phone."
    sm "Oh my god, really?! You’re here?! Give me a second, I’ll be there in a jiffy!"
    mc "I’m just at the{nw}"
    $ _history_list[-1].what = "I’m just at the—"
    "And she drops the call."
    "Perfectly timed, as all things should…"
    "Does she already know where I am…? Only God knows, so I just continue sitting on the bench and carry on playing a visual novel I forgot to finish eons ago."
    return