label albert_study:
    play music "sound/bgm/Sketchy Logic - Shop of the Arcane.mp3" fadeout 0.7 fadein 0.5
    scene albert_study with fade
    show luna at left with dissolve

    "Albert sits smugly at his overly ornate desk, toying with his latest creation. The delicate glass bird has so much detail no artisan could ever have crafted it."

    a "Now here's a visit I wasn't expecting. To what do I owe the pleasure?"

    l "(If I leave it up to him, this conversation will last forever and go nowhere... I'll cut to the chase. If anything, that just might unsettle him enough that he'll let something slip.)"

    "Luna holds up the recording sphere."

    l "This."

    "Surprise flashes across Albert's face, but he swiftly recomposes himself."

    a "Might I ask what you were doing there?"

    l "(I can't tell if he's not denying it, or if he's fishing for information by being purposely vague...)"

    l "I could ask you the same thing. Ladies first, isn't that what you always said?"

    "Albert gives her a perfect, charmingly fake smile."
    a "Let's compare notes then. Where did you find it?"

    l "(Ugh. Really? We're going nowhere fast like this, are we? Fine.)"

    l "Nikolai's house. Your turn."

    a "I've always had an interest in the case. How about you?"

    l "(Looks like I can't avoid being blunt here...)"

    l "I have reason to believe Nikolai was framed. But I was friends with him. Why would you care about him?"

    a "Why Luna, he and I worked together for years. Isn't it only to be expected that I would care?"

    l "I don't recall you standing up for him much back then... Stop playing games, Albert."

    "Albert watches her carefully for a long moment, then sighs."
    a "I am not playing games, Luna. You may not know this, but at the time of his death, Amarov was investigating the Council for a series of murders at the request of the Aylan branch."

    "Luna tries hard to hide her surprise."
    l "(What?! Wasn't it supposed to be a secret?)"

    a "The truth is, House Lycioe was originally supposed to run the investigation. A neutral outside party, you understand."

    l "(As neutral as they can be with you in the Council.)"

    a "But we were spread too thin at the time. Instead, we passed it on to two members who were known to be neutral in Council politics. Amarov and Crowe."

    a "Long story short... It has always seemed like too much of a coincidence that one of them was executed and the other failed to make any progress in the investigation."

    l "That's funny. Did you manage to fit all your protests at the trial while I was off on a bathroom break? Because I don't remember you saying a word of that."

    a "I have a reputation to uphold, Luna. If I made any comments and turned out to be wrong, it would be a stain on the Lycioe name."

    l "And it's not a stain to let an innocent man die?!"

    a "I didn't know he was an innocent man! I still don't. That's why I was looking into it, alright?"

    a "I need to know that we didn't inadvertently cause his death by giving him the case."

    l "What a load of bullshit."

    l "You really expect me to believe that?"

    l "(A powerful family like his, siding with Nikolai? If there was ever a definition of too good to be true...)"

    a "Believe me or not, that's your prerogative. But I need the sphere back, Luna. It's evidence. I can show you the recording if you want, but I need you to return it now."

    l "(So that's what it's about, is it? Getting your hands on it?)"

    show luna at Position(xpos = 0.15, xanchor = 0.5) with MoveTransition(0.5)

    "Albert reaches for the sphere, but Luna backs away."

    l "(It's got me talking to Nikolai in it! No one is ever going to believe he's not a necromancer if they see him back as a ghost... And that's just asking to get myself accused too!)"

    a "Luna, give it back!"

    "Albert summons the sphere to himself with his magic."

    with flash
    "In a panic, Luna shatters it in midair."

    l "(Oh crap. Now I've done it.)"

    l "(But I didn't have a choice. I couldn't let the Lycioes have it!)"

    "Albert stares in shock."
    a "Luna..."

    l "I, uh... I need to go."

    "Luna runs out before Albert can stop her."
    hide luna with moveoutleft

    l "(I need to make sure the preparations are ready to go back to the demon realm... There's no telling what the Lycioes might do as payback. Divines damn it!)"

    jump council_albert_absent
    return


label council_albert_absent:
    scene council_room with fade
    "The High Mages are gathered around the large, circular meeting table. Eilhart is leaning back on his chair with his feet propped up on it. Albert is conspicuously absent: everyone half expects him to start shouting at Eilhart, and the silence is unsettling."

    show eilhart at right with dissolve

    e "Where is that pompous redhead? He should've been here already. In all of my tenure, I've never seen him be late for council."

    ca "Mmmhh. You, on the other hand, are always late."

    e "And you oversleep more often than not, dearest Pot."

    v "What a waste of time."

    #TODO play knocking sound

    "A knock interrupts them. Serach pokes his head in, looks around and shakes his head."

    e "What is it, Serach?"

    se "High Mage Lycioe's apprentice asked me to check if he was here... He was supposed to meet him before the council meeting to give him his tasks for the day, but he never showed himself."

    l "(That's not like him...)"

    se "His family has been asking about his whereabouts as well. I'll have to inform them that he's not here."

    e "Feh. He's probably gone to meet some lover or something. No need to make such a fuss."

    ca "He wouldn't. Not with the fiancée he has. He's been pestering me for weeks for a reading on when best to marry her..."

    e "Then maybe he's looking for a ring or something equally expensive and yet worthless."

    e "He's a big kid. The pride of the family. He can take care of himself."

    v "I have my doubts."

    show luna at left with dissolve

    l "It is unusual that he would be so late."

    r "Ah, give the boy a break. It would be good if he finally decided to loosen up. He's so stuffy I'm amazed his shirt collar hasn't strangled him yet."

    l "(That's my Grandfather. But still...)"

    e "Do we postpone the session or go on without Mr Truantyoe?"

    l "(Please tell me you didn't make that pun.)"

    l "Regardless of whether we continue or not... We should send out people to look for him."

    v "I bet we'll discover he was asleep at his desk... or better yet, trying to find Eilhart to make sure he isn't late."

    v "And it would be ironic because today you were almost on time."

    e "Yeah, yeah. Blame the blonde, won't you. Alright, let's just send some mooks."

    stop music fadeout 3.0
    scene black with fade

    "But as the day wore on and no word came of Albert Lycioe, the atmosphere grew heavy. Caers muttered of ill omens in the stars, warning him for days on end, Victoria was snappier than ever, and even Readak and Eilhart's jokes grew rare. Luna couldn't help this heavy feeling..."

    jump graveyard
    return


label graveyard:
    scene graveyard with fade
    play music "sound/bgm/Darren Curtis - Hallow's Eve Ritual.ogg" fadeout 0.7 fadein 0.5
    "The High Mages are standing in the graveyard of a small neighboring town. A green-faced Caers is emptying his breakfast on a nearby tree. The sound of metallic hooves signal Eilhart's approach as he rides one of his automatons."

    show eilhart at right with dissolve

    e "What happened here? I came as fast as I could."

    ca "They f-found him..."

    e "What do you mean, 'found' him?"

    "Eilhart pushes past a crowd of many redheaded Lycioes to get to the hole they were all gathered around. Readak is holding Luna as she shakes uncontrollably."

    e "...Oh."

    e "Caers, any room left near your tree?"

    "Albert's hair pales in face of the blood coating all over his robes. It has pooled under his chest, where countless stab wounds have torn fabric and flesh alike."

    "Two black candles burn over each of his hands, and countless necromantic runes have been drawn all over his too-white skin."

    show luna at left with dissolve

    l "(Albert... Oh Divines. How...?)"

    r "Luna, it's okay. There wasn't anything we could do."

    l "(Wasn't there? What if I caused this somehow? What if...)"

    l "(Oh no. The broken sphere. There's only one person he could get help from to fix the enchantment...)"

    l "(Could it be... Eilhart...?)"

    "Luna looks back at Eilhart warily. Too late, she realizes he isn't the one that is being watched with suspicion."

    l "(No... Did the tail they set on me see me studying necromantic artifacts? They can't possibly think I did this...)"

    e "News travel fast, don't they?"

    "A redhaired woman whose features are strikingly similar to Albert's walks in, accompanied by some of her family."

    e "Vera. I'm really sorry."

    l "We all are... Please, let us know if you need--"

    "But Vera brushes past them, too anguished to reply. She rushes to her brother's side, kneeling near the shallow grave in horror."

    ve "Albert... No..."

    "They all watch as the grieving Vera places her hand over Albert's eyes. Closing her own, her body shakes with silent sobs as magic builds around her hand."

    with Fade(0.5, 0.1, 0.5, color="#852ffa")

    l "(Right, she's a diviner... At least we'll know who did this.)"

    v "What did you see?"

    ve "I would speak of it privately."

    "But the damage is already done. Grief-stricken, angry eyes sought their target faster than she could restrain herself."

    "Luna feels her stomach twist."

    l "W-What? Why are you looking at me like that?"

    show luna at Position(xpos = 0.18, xanchor = 0.5) with MoveTransition(0.5)

    l "I-I didn't--"

    l "(Oh no...)"

    v "Eilhart, won't you escort Luna back to headquarters?"

    l "No!"

    l "(This can't be happening! How... Are the Lycioes in on this? How could Vera be fooled? Why...?)"

    l "(I can't... Oh Divines, any trial at this point is going to be even more of a farce than Nikolai's was.)"

    "Eilhart motions to one of his automatons and it follows him closer to Luna as he approaches her."

    show eilhart at Position(xpos = 0.70, xanchor = 0.5) with MoveTransition(0.5)

    e "Come on, Luna. Let's talk about this back in the Guild."

    "But Luna shakes her head and releases the spell she'd been casting. Dark tendrils snake up from the tombstones' shadows and wrap themselves around Eilhart's legs and then the automaton's, holding them in place. Luna takes off running desperately."

    with Fade(0.3, 0.2, 0.5, color="#393939")
    $ renpy.pause(0.3)
    hide luna with moveoutleft

    l "(I have to get to Sola and Alice...!)"
    jump sola_house
    return

label sola_house:
    play music "sound/bgm/Darren Curtis - Unnerving Chase.ogg" fadeout 0.7 fadein 0.5
    scene sola_house with fade
    show luna at left with dissolve

    "Luna is holding Sola's hand while they both run into the woods nearby, little Alice holding on tightly as Sola carries her as well as she can."

    l "Quick! Through here! Oh Divines, they're here, we've got to get them off our trail!"

    hide luna with moveoutright

    scene woods with fade

    show luna at left with moveinleft

    alc "Mama, what's going on?"

    s "Shhh! I'll explain later!"

    with Fade(0.5, 0.1, 0.5, color="#393939")

    "Luna conjures up a shadow mist to try and shake their pursuers, but they can still hear them coming closer."

    l "Come on! We're almost there. We just need to get to the anchor point and it'll take us right to the portal!"

    "Luna takes Alice from Sola so they can run faster. Just as they start losing their pursuers, the sound of crackling and whistling air is the only warning before one of Victoria's fireballs comes hurtling their way."

    #TODO play a high pitched scream and explosion

    with Fade(0.5, 0.1, 0.5, color="#f09400")
    with hpunch
    with tintred
    stop music

    l "SOLA!!!"

    "Luna stands there in shock, wide eyed and clutching Alice tight to her chest. Sola lies fallen on the ground, the smell of charred flesh overwhelming as smoke rises off her back."

    play music "sound/bgm/Alexandr Zhelanov - Deal with the Devil.mp3" fadeout 0.7 fadein 25.0

    l "So...la.... No, this can't..."

    alc "Mama...?"

    "Luna falls to her knees."

    l "My twin. No. No. She's always been here. She can't be... No. No!!"

    alc "Mama!"

    "Alice tries to squirm out of her aunt's arms, reaching out for Sola. Luna wails and holds on tightly."

    #TODO play footsteps sound

    "The sudden sound of footsteps makes her head snap up just as her hands light up with an angry, purple glow."

    "She stops when she recognizes Emil."

    l "E... Emil... Sola, she..."

    l "She's alright... Right? She can't... She can't be..."

    "Emil takes one look at Sola and winces. He reaches for Luna instead, trying to help her up."

    em "There's nothing you can do. You have to go now!"

    l "I can't leave her!!"

    em "Luna!"

    l "She's my twin! She's half of me!"

    em "Just go!"

    l "SOLA!"

    "Emil hugs Luna tightly, so much Alice has to whine and protest. He then shoves Luna back hard."

    show luna at Position(xpos = 0.16, xanchor = 0.5) with MoveTransition(0.15)

    em "You have to do this, Luna. For Sola's sake. She wouldn't want you to get caught. You can't let Alice get hurt!"

    l "B-But... I..."

    em "I'll point them the wrong way. Save her daughter! Go!"

    $ renpy.pause(0.5)
    hide luna with moveoutleft

    scene black with fade

    "Luna safely escaped to the demon realm with her niece and settled where she could keep Dmitri company."

    "But part of her was left behind that day: without Sola, she was never the same. And though she did her best to raise Alice as her sister would have wanted, she looked to the future with a singular, dark determination."

    "For she vowed this to Dmitri the day she got back: once he and her niece had no longer need of her, she would go back, and she would avenge Nikolai and Sola. One day..."

    $ renpy.pause(0.5)
    show text "Ending 2 of %d" % (numEndings) with dissolve

    $ renpy.pause()

    hide text with dissolve

    return