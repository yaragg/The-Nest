label eilhart_study:
    play music "sound/bgm/Darren Curtis - Fireside Tales.ogg" fadeout 0.7 fadein 0.5
    scene eilhart_study with fade
    show eilhart at Position(xpos = 0.85, xanchor = 0.5)
    show emil flip at Position(xpos = 0.48, xanchor = 0.5) 
    with dissolve
    "Luna walks into Eilhart's study and is surprised to find Emil already there."

    show luna at Position(xpos = 0.13, xanchor = 0.5) with dissolve

    l "Huh? Emil, what are you doing here?"

    em "(surprised)\nLuna?"

    "Emil quickly motions to his mechanic arm."

    em "Oh, I'm just getting my arm checked out. It's a wonder how it never broke while we were away."

    e "Please do come in, knocking is for weaklings. I'm fine, thanks for asking. How are you?"

    l "Right. Sorry. Eilhart, there's something I need to discuss with you."

    l "(But first...)"

    # ![[Player choice

    menu:
        "Ask to speak in private.":
            jump emil_leaves
            return

        "Let Emil stay.":
            jump emil_stays
    return



label emil_stays:
    l "Emil, you can stay. I think I'd feel better with you here."

    "Emil smiles."
    em "Of course."

    e "So what did you want?"

    "Luna shows him the recording sphere."

    l "I found this. I couldn't get past the protective charm, but I was hoping you could work your magic... In both senses."

    e "(surprised)\nThis is quite the piece. Where did you find it?"

    e "Wait... This is Lycioe's work, isn't it? It's got his style all over it. Why do you have this?"

    l "(Well, that's one cat out of the bag.)"

    if(heardEilhartStory): 
        l "(Eilhart is on my side. There's no point in lying now. Besides, if I lie to him now, I'll be lying to Emil too.)"

    else: 
        l "(I can't really ask him for help and not tell him. He might figure it out anyway if he gets a glimpse while breaking the ward... Besides, if I lie to him now, I'll be lying to Emil too.)"

    l "I found it in the old Amarov house."

    "Eilhart freezes for a moment, then continues to reach for the sphere and takes it."

    l "(What was that?)"

    "Luna exchanges looks with Emil."

    l "(He seems nervous... I guess he noticed Eilhart's reaction too.)"

    e "What were you even doing in there?"

    if(toldEilhartAboutDmitri or heardEilhartStory):
        l "I was there for my investigation. I found it hidden in one of the bookshelves..."

        l "Given how influent the Lycioe family is, I wouldn't be surprised if they had Nikolai silenced about something. It certainly looks that way, if Albert was worried enough to keep surveillance in the house."

        em "Wait, you told Eilhart about it?"

        l "That I was investigating? Yeah."

        em "Are you sure that was smart? You don't want the Council knowing, Luna."

        l "Well it's kind of too late to argue the point now."

        e "Erm... Guys, I'm still here."

        l "Right. Uh, the sphere. Have at it."

    else:
        "Luna smiles sadly."

        l "Just reliving some old memories, I guess."

        l "In any case... Here you go."

    "Luna hands Eilhart the recording sphere. He walks over to his desk to examine it, and motions at Emil in the meantime."

    e "Look the door, will you? I assume we don't want Lycioe walking in on this."

    em "Sure."

    "The door locks with a click. Luna can't help but feel Emil looks uneasy, before she turns away to look back at Eilhart."

    e "Right. I can see he's a creation mage, not an enchanter. If I go through this gap in the ward here..."

    "Eilhart fiddles with the sphere for a moment, his hands glowing slightly. He reaches inside his desk for something."

    e "Luna, can you help me for a sec?"

    l "Uh, sure."

    show luna at Position(xpos = 0.4, xanchor = 0.5) with MoveTransition(1)

    "Eilhart glances nervously at Luna, then back at Emil. As Luna walks closer to Eilhart, reaching for the sphere, she sees the cold sweat beading above his lips."

    l "(What--)"
    stop music fadeout 0.1

    "Eilhart makes a stab with the paper knife he was holding."
    play music "sound/bgm/Sketchy Logic - Taste My Blade.mp3" 

    # show luna behind eilhart
    # show emil flip behind luna
    show emil flip behind eilhart
    show eilhart at Position(xpos = 0.62, xanchor = 0.5) with MoveTransition(0.4) 
    show luna behind emil with flash

    l "Ahh!"


    "A terrible metallic screech sounds as Emil pushes her out of the way. Mechanical arm raised, he blocks the strike and grimaces as the paper knife embeds itself in his arm."

    l "Emil! Are you--Eilhart, are you insane?!"

    with Fade(0.3, 0.1, 0.5, color="#393939")

    "Luna's hands swirl with dark magic and she lashes out at Eilhart. He blocks it with a quick shield, which shatters and crumbles under her magic."

    l "(This doesn't make sense! Why would he do this?! Is he on the Lycioe's payroll?)"

    l "(He didn't think this through. We're two against one--)"
    "Luna's eyes go wide with realization."
    l "(Oh crap.)"

    e "What are you doing?! Kill her!"

    "Luna turns to Emil in horror."

    l "(That arm is Eilhart's work. He saved Emil's life that day. If anyone has the power to turn Emil's magic on us...)"

    "Emil yanks the knife out of his arm."

    l "Please, Emil, you have to fight it off..."

    "Emil grips the knife tightly, trembling..."

    "Then promptly turns and stabs Eilhart."

    show emil flip at Position(xpos = 0.56, xanchor = 0.5) with MoveTransition(0.1)
    with tintred

    l "(What?!)"

    "Emil stabs him over and over, in a fury."
    show emil flip at Position(xpos = 0.48, xanchor = 0.5) with MoveTransition(0.1)
    show emil flip at Position(xpos = 0.56, xanchor = 0.5) with MoveTransition(0.1)
    with tintred
    show emil flip at Position(xpos = 0.48, xanchor = 0.5) with MoveTransition(0.1)
    show emil flip at Position(xpos = 0.56, xanchor = 0.5) with MoveTransition(0.1)
    with tintred
    show emil flip at Position(xpos = 0.48, xanchor = 0.5) with MoveTransition(0.1)
    show emil flip at Position(xpos = 0.56, xanchor = 0.5) with MoveTransition(0.1)
    with tintred


    l "E-Emil! Stop!"

    "But he doesn't. Luna tries to pull him off Eilhart, but by the time she manages to overpower him, it's too late."


    hide eilhart with easeoutbottom
    show emil flip behind luna

    l "What... What did you do?! Emil, h-he's dead!"

    show emil at Position(xpos = 0.54, xanchor = 0.5)

    em "He tried to {i}kill{/i} you!"

    em "He tried to make {i}me{/i} kill you!"

    "Luna hugs him tightly, and takes the knife off his hands."
    play music "sound/bgm/Alexandr Zhelanov - Welcome to old manor.mp3" fadeout 3 fadein 1.5

    l "Just... stop..."

    em "I-I'm sorry..."

    "Emil takes a deep breath, trying to calm himself and stop shaking."

    em "We can... We can argue self defense. It was nothing but that, really."

    l "But why...? Why would he do this?"

    "They exchange looks and turn to the recording sphere lying on the ground beside Eilhart."

    l "Could it be...?"

    "Luna gingerly avoids stepping on blood as she reaches for the tiny sphere. It seems to glow almost tauntingly at her."

    l "The cause of all this..."

    "With the ward dispelled, Luna activates the sphere."

    #Show Nikolai's house bg superposed over the current bg]] 
    show nikolai_study_record behind luna, emil with fade

    "Luna speeds through the footage of the empty house, until--"

    l "Eilhart."

    show eilhart_record at Position(xpos = 0.85, xanchor = 0.5) with dissolve

    l "What's he doing there?"

    em "It's like he's looking for something..."

    em "Or making sure we don't find it."

    l "You think he's...?"

    em "What else would explain this?"

    em "(sighs)\nOh, Luna, you had to go straight to Nikolai's killer..."

    em "Talk about not making enemies."

    l "He knew what we would find if we saw the recording..."

    l "So that's why he tried to kill me? But something just seems wrong..."

    em "What do you mean?"

    l "I don't know. Maybe it's just that it feels too simple."

    l "I've been looking for so long... And this is how it ends?"

    l "A body in an office... And no answers at all."

    em "But it is an answer, Luna. Eilhart did this. He's the reason why Nikolai is dead."

    em "Maybe it doesn't tell you why he did it, but... Dead men tell no tales. It's the best we can do."

    em "At least Nikolai can rest in peace now..."

    l "(If only he knew. I just wish I could give Nikolai an answer...)"

    em "Come on, let's call this in. I'll need your help..."

    #[[Slowly fade to black]]
    scene black with longfade

    "There wasn't a day Luna didn't ask herself why, until time slowly erased the question. After she and Emil reported their findings to Nikolai, he vanished, never to be seen again."

    "Luna couldn't quite shake the feeling that she'd missed something. But that, too, faded over time--Luna and Emil were too busy, having elected to stay in the Guild to clear it of its corruption."

    "Luna still visited Dmitri in the other realm sometimes, but she knew her place in the Council at Emil's side, where they could work to make sure there were no more Nikolais, ever again."

    em "That was a close one, Luna."

    em "I don't know what I would have done if you'd found out..."

    $ renpy.pause(0.5)
    show text "Ending 3 of %d" % (numEndings) with dissolve

    $ renpy.pause()

    hide text with dissolve

    return


label emil_leaves:
    l "Emil, could you give us a second?"

    em "Huh? Sure. That's it for my arm, right? I'll catch you later, Elly."

    "Emil gives her a look that plainly translates as {i}\"What are you getting yourself into this time?\"{/i} but leaves all the same."

    hide emil with dissolve

    e "Well that wasn't rude."

    l "What, my interrupting or his calling you pet names?"

    e "Now that you mention it..."

    "Luna just laughs, but before long the weight of the recording sphere in her hand makes her sober up again. She hands the sphere over to Eilhart."

    l "I found this. I couldn't get past the protective charm, but I was hoping you could work your magic... In both senses."

    e "(surprised)\nThis is quite the piece. Where did you find it?"

    e "Wait... This is Lycioe's work, isn't it? It's got his style all over it. Why do you have this?"

    l "(Well, that's one cat out of the bag.)"

    if(heardEilhartStory): 
        l "(He's on my side. There's no point in lying now.)"

    else:
        l "(I can't really ask him for help and not tell him. He might figure it out anyway if he gets a glimpse while breaking the ward...)"

    l "I found it in the old Amarov house."

    "Eilhart freezes for a moment, then continues to reach for the sphere and takes it."

    l "(What was that?)"

    e "What were you even doing in there?"

    if(toldEilhartAboutDmitri or heardEilhartStory):
        l "I was there for my investigation. I found it hidden in one of the bookshelves..."

        l "Given how influent the Lycioe family is, I wouldn't be surprised if they had Nikolai silenced about something. It certainly looks that way, if Albert was worried enough to keep surveillance in the house."

        e "You might be right. They've got their fingers in a lot of pies for sure."
    else:
        "Luna smiles sadly."
        l "Just reliving some old memories, I guess."

    l "In any case... Here you go."

    if(heardEilhartStory):
        jump eilhart_trusts_luna
    else:
        jump eilhart_doesnt_trust_luna

    return

label eilhart_doesnt_trust_luna:

    "Luna hands Eilhart the recording sphere. He sits at his desk and fiddles with it, frowning deeply."

    "After a solid fifteen minutes of tinkering, he shakes his head."

    e "I can't do it."

    l "What?"

    l "You're a master enchanter. If you can't break that ward, who can?"

    e "Don't ask me. Looks like the Lycioes have a trick up their sleeves, that's for sure."

    e "But I can come up with something if you give me more time. I'll keep the sphere and work on it some more."

    e "If I still can't do it after a couple of days, I'll give it back to you."

    l "...Alright."

    l "(It's not ideal, but if the Lycioes bothered to place such a strong enchantment on it, I want to find out what's in it even more.)"

    l "Thanks for this, Eilhart. I'll owe you one."

    e "You can buy me lunch sometime."

    l "You're gonna pick a super expensive restaurant, aren't you?"

    "Eilhart grins."

    e "Perish the thought!"

    scene black with longfade

    "But Luna would never have to worry about that. The next day held an unpleasant surprise..."

    $ eilhartKeptSphere = True
    jump council_albert_absent
    return

label eilhart_trusts_luna:
    "Luna hands Eilhart the recording sphere. But instead of working on it, Eilhart just sits at his desk, turning the glass sphere in his hands deep in thought. Seemingly having made a decision, he lets out a heavy sigh."

    l "What is it?"

    e "I'll be honest..."

    "Eilhart meets her gaze."

    e "I already know what you're going to see in this thing."

    l "...What?"

    e "You'll see me, looking for evidence."

    l "Evidence? You mean you--"

    e "Not for an investigation. To destroy it."

    l "What?!"

    l "(He's just going to admit to it?!)"

    l "Eilhart, did you... Did you frame Nikolai?"

    "Eilhart is silent for a moment. Finally, he sets down the sphere and looks back at her."

    e "Am I involved in the frame job? Yes. But am I the one who did it?"

    e "No."

    e "But you could say I'm the... cause, I guess."

    e "I've got another story for you. The other one wasn't a lie--but it was... Heavily edited."

    e "This time, I'll give you the truth, and nothing but the truth."
    e "But I'll tell you now, you won't like it."

    e "Will you hear me out before you make your judgment?"

    l "What kind of question is that? I didn't come so far to run from the truth when I found it. I want answers..."

    "Eilhart smiles wryly."

    e "Then lock the door and take a seat. It's storytime."

    scene black with longfade

    e "You know how I shot up the ranks way back?"

    e "I had help."

    e "You see, at some point after I joined, I found a man under attack..."

    e "I saved his life. But his arm couldn't be salvaged, so I had to make him one too."

    l "Wait. Arm? That sounds like..."

    e "Exactly who you're thinking of."

    l "Emil? What does he have to do with anything?"

    e "Apparently nothing. You'd think that, anyway..."

    e "From that moment on, people were afraid. Word got out that I practically owned Emil now. For someone with his kind of magic, owing me his life means he basically has to do anything I say, right?"

    e "I thought I struck it big. That's the mistake they all make. A few months after that, Emil came to my office..."


    play music "sound/bgm/Darren Curtis - Come Out And Play.ogg" fadeout 0.7 fadein 0.5
    scene eilhart_study_past with fade
    show eilhart at right with dissolve

    "A knock interrupts Eilhart's work."

    e "Yeah? Come on in."

    show emil flip at left with dissolve

    "Emil walks in and closes and locks the door behind him."

    em "I know who you are."

    e "...Excuse me?"

    em "Ernest Talbot."

    "Eilhart pales."

    e "How..."

    em "A magician never reveals his secrets, right?"

    "Eilhart clenches his fists."

    e "...What do you want?"

    e "I saved your life, you ingrate."

    em "Oh no no, I'm not here to threaten you. On the contrary. Your secret is safe with me."

    em "As you said, I owe you my life. So this is me repaying the favor."

    em "There's some of the other senior enchanters... They're onto you."

    e "What?"

    em "They've been suspecting you for a while now. Derek Calcino and Thomas Cassar. Those are the names."

    em "They're going to be canvassing your neighborhood a few days from now. They'll find your shop..."

    e "(Oh, shit. I can't let that happen. Not with her and the kids in there. And they're too sick to move...)"

    em "This is all I can do. I'll leave you to it..."

    "Emil leaves before Eilhart can say anything else."
    hide emil with dissolve
    # show luna at Position(xpos = 0.13, xanchor = 0.5) with dissolve
    $ renpy.pause(1)
    jump eilhart_study_back_present
    return


label eilhart_study_back_present:
    play music "sound/bgm/Alexandr Zhelanov - Rooms.mp3" fadeout 0.7 fadein 0.5
    scene eilhart_study with fade
    show luna at left
    show eilhart at right
    with dissolve
    l "What... What did you do?"

    e "The only thing I thought I could do."

    "Eilhart smiles sadly."

    e "I... killed them."

    l "Eilhart!"

    e "What else could I do? I didn't have a choice, Luna! It wasn't right, what I did. I'll be the first to admit it."

    e "But I just... I didn't know what to do. There was no one to help me and my family depended on it. I forced myself not to dwell on it..."

    e "But I should have. You see, a few months later, Emil came back."

    e "He told me people were investigating their deaths. And I panicked even more."

    e "Now I wasn't just some man with motive enough to hate the Council going undercover... I was a murderer."

    e "If someone found out..."

    l "(narrows her eyes)\nYou killed them too."

    e "I couldn't think straight. I was in a panic. Thinking back on it, he probably counted on that."

    e "I thought he was just trying to clear his debt. You know, help me out on his own terms rather than wait for me to demand the favor back my way."

    e "That's the other mistake everyone makes when it comes to Emil."

    e "We all think his power is about being morally higher than us... Help us out so we owe him, don't wrong us."

    e "But you don't need to outswim the shark. Just the guy next to you."

    e "He doesn't need to be good, so long as we're worse. He never told me to kill them... I made the decision myself."

    e "But before I knew it, he owned me. Sure, I saved his life, but how many times did he save mine by keeping my secret? Once for each man I killed?"

    e "By the third time he came back, I started suspecting. Rather than panic, I looked into the names he gave me. That's when I realized they had never been investigating me."

    e "He just used me to get rid of the people who might be trouble to him someday. But it was too late. Even if he fooled me, I was in it too deep already."

    e "I think... Part of me liked it, what I did. It was horrible, and wrong, and I hated it, but..."

    e "Those were the people who'd denied me help. I was alone, and powerless... I tried and tried each day to help my family but they just kept getting worse and no one would even care."

    e "I was just so angry. It doesn't excuse what I did, but I did it anyway. It made me feel empowered... Like I was even a tiny bit in control of my life again."

    e "Emil picked up on it. He said, if I was going to kill anyway... Why not make a good thing out of it? Why not use them to figure out how to help my family?"

    l "No. Stop. Emil wouldn't do any of this."

    l "He's not that kind of person!"

    l "He's sweet, he's loyal, and he lov..."

    e "Lies all the freaking time? If you really don't believe what I'm saying, why didn't you speak up way earlier before I spent three years worth of breath on a stupid monologue?"

    e "The guy's a monster, Luna."

    l "So are you if any of that was true!"

    e "That's not the point! Look, you wanted Nikolai, didn't you? I'll get to it."

    e "Emil offered to help me. I didn't have much to lose by taking him up on his offer at that point."

    e "We tried all sorts of research... Spells, rituals, anything we could get our hands on. Dark stuff that would give even your grandfather nightmares."

    e "That's when we figured out how to trap souls in inanimate objects. He came with some Necromancy tome and we adapted a lich-making ritual..."

    e "We sealed a soul in a gem instead, and attached it to a magical, metallic construct. By building complex magic circuits, the energy from the gem made it move..."

    l "(eyes go wide)\nYour automatons."

    e "Yeah."

    l "They're powered by souls?!"

    e "Each and every one of them. I hoped to improve on them and build new bodies for my family..."

    e "But of course all those disappearances started attracting attention."

    e "By then, Emil had already helped me up the ladder and gotten me into the Council. I found out two of our members were looking into our victims..."

    l "...Crowe and Nikolai."

    e "(nods heavily)\nI panicked like I hadn't in so long. I went straight to Emil. Told him we were done for, we were going to be exposed..."

    e "He just said, \"Don't worry about it.\""

    e "The next day, that anonymous tip came in."

    l "...No. No, it can't be. Emil couldn't."

    e "He did. He got that Necromancy stuff from somewhere before... He knew how to do it again."

    e "And he's been really good about playing you all this time. Why do you think he was here anyway? We were discussing how to handle you because you wouldn't back down."

    l "You're lying!"

    e "Try me. I'd tell you to ask him yourself, but the moment he figures out I betrayed him, I'm done for."

    e "He could easily make me go after my own family..."

    e "I trust you, Luna. It's why I told you all this. I..."

    e "I need your help."

    l "You've got to be kidding me."

    e "This is my only way out. Please."

    e "You get Nikolai's killer, and I get my freedom again."

    l "Freedom to keep on killing?!"

    e "Freedom to get my family the hell out of here!"

    e "When you guys left for the other realm, I thought of I was free of him. But then he came back."

    e "I can't do this anymore. When it's just me, I feel like I can do better. Like I'm not some sick psycho. But when he's around..."

    "Eilhart just shakes his head."

    e "I want to do better. I want to fix my family... I don't want to do this anymore."

    e "When your reports mentioned some of the kinds of magic they had in that realm, I thought... Maybe I could try that. Maybe they have something. Some cure... Anything."

    l "Maybe some things aren't meant to be cured, Eilhart."

    e "Easy for you to say when you don't have to watch the love of your life and your flesh and blood wither and rot in front of you."

    menu:
        "\"I'll help you.\"":
            jump help_eilhart

        "\"You're no better than the man who did this to your family.\"":
            jump turn_eilhart_in
    return


label help_eilhart:
    l "...Alright. I'll help you."

    l "You're a murderer. Nothing's going to change that."

    l "But I think we both know who the greater evil here is."

    l "(I just... Why would Emil do this? I want to believe Eilhart is lying, but for this to be such an elaborate lie...)"

    l "(Could I really have been this blind? Emil...)"

    e "Then meet me in the shop tonight. We need to figure out how to deal with him. Exposing him to the Council isn't going to do shit, not with the dirt he's probably got on them."

    l "Maybe they'd be glad to be rid of him."

    l "(But Eilhart would still be in danger from his magic. And I doubt Emil would go down without dragging him along too...)"

    l "(Maybe that would be the way to go. Bringing them both to justice. It just feels like there's no right answer here...)"

    l "Oh I have my own idea. I say we get him to go back to the demon realm with me."

    l "He can't be tried here... But he can over there."

    l "The vampires will put him on trial. Maybe Dmitri himself will get to decide the verdict. It would be fair thing to do."

    e "He'd never see it coming either. I can work with this..."

    e "Thank you, Luna. Maybe I'll finally be able to put this all behind me."

    l "You do that. None of this should ever have happened..."

    scene black with longfade
    $ renpy.pause(0.5)
    show text "Ending 4 of %d\nTo be continued..." % (numEndings) with dissolve

    $ renpy.pause()

    hide text with dissolve

    return

label turn_eilhart_in:
    l "No. You're no better than Korone."

    e "...What?"

    l "Killing people who have nothing to do with you. Taking pleasure in it."

    l "No matter what motives you may have, I can't play along with that."

    l "How many wives did you murder, Eilhart? How many children? How many Eilharts did you leave out there?"

    e "You're not... I..."

    l "You know I'm right. Do you really think your wife would want you to do this for her?"

    l "This isn't who you are. Or at least... It's no who you were, once."

    l "I don't know what you are now."

    l "But I know you have to be brought to justice."

    "Eilhart puts up almost token resistance, diving at Luna with a paper knife she isn't sure he really wanted to find its mark."
    "When she tells him she'll look after his family, he breaks."

    scene black with longfade

    "When the trial comes, Eilhart is eerily silent. He doesn't breathe a word about Emil, or his family, or any of the story he's told her. He simply confesses to the murders and to framing Nikolai and blackmailing Crowe to stop their investigation."

    "Eilhart is put to death. But without his testimony, there is no way to ever prove Emil's involvement..."

    "Part of Luna can't bring herself to believe that the man she'd cared for so deeply--loved--could have done this."

    "The other part can't ever look at him the same again. Maybe one day, she will have the courage to confront him. But with her own family to protect and no justice to turn to, she fears she may become another Eilhart herself..."

    $ renpy.pause(0.5)
    show text "Ending 5 of %d" % (numEndings) with dissolve

    $ renpy.pause()

    hide text with dissolve

    return