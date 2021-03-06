define sm = DynamicCharacter('sm_name', image='sayonika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mi = DynamicCharacter('mi_name', image='mio', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define b = DynamicCharacter('b_name', image = 'baker', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define b2 = DynamicCharacter('b2_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ssm = Character("Sayo & Sayo", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mrc = Character("Mr. Cow", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# Special case for Yuri
image yuri 2by7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
