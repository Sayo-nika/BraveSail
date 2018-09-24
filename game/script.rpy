# Entry point
label start:

    # ID of this playtrhoguh
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    python:
        s_name = "Sayori"
        m_name = "Monika"
        n_name = "Natsuki"
        y_name = "Yuri"
        sm_name = "Sayonika"
        mi_name = "Mio"
        b_name = "Baker 1"
        b2_name = "Baker 2"


    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True


    if persistent.playthrough == 0:
        $ chapter = 1
        call ca1
        call ca2
        call ca3
        call 
        scene black
        call screen ThrowASError(error_type="ACT_FAULT_IN_NONACT_AREA")
    else:
        scene black with dissolve_scene_full
        call screen ThrowASError(error_type="ACT_FAULT_IN_NONACT_AREA")
        pass

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
