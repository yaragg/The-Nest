label luna_office_letter:
    scene luna_study with fade
    show luna with dissolve
    "Luna is hard at work reviewing evidence."


    #TODO Play knocking sound

    # scene luna_study with flash
    show luna with vpunch
    "Luna jumps in surprise and scrambles to hide her papers."


    l "Come in."

    #TODO play paper rustle sound

    "A note is slid out from underneath her door. Luna frowns as she picks it up."
    # show luna with vpunch

    l "An ad...?"

    #TODO show ad picture

    "~ Moonlight Woods ~\n
    Furniture, signs, dolls, anything that requires skill and quality--bring it to us.\n
    246 Ailey Street"

    "Luna almost laughs at the sheer normalcy of the ad."

    l "An ad. Oh Divines, what did I think it was? I'm far too worked up..."

    l "But still... No ad magically finds its way under a High Mage's door like this."

    l "Someone wants to meet with me, and I'm curious who it is."

    "Luna carefully clears her desk of any evidence and leaves."
    jump meet_with_eilhart
    return


label meet_with_eilhart:

    scene eilhart_shop with fade
    show luna at left with dissolve
    
    "Luna looks around the shop, impressed with the realism of the dolls displayed."

    l "I would buy one for Alice if they weren't so creepy..."

    "Luna walks up to the counter and hands the ad over to the old man working there."

    l "This found its way into my office."

    "The old man smiles."

    o "He's waiting in the workshop."

    l "(He...? Well, let's see who this secret admirer is...)"

    hide luna with dissolve

    scene eilhart_workshop with fade

    show luna at left with dissolve

    "Eilhart is hunched over a table working on a doll, and straightens back up to look at Luna as she comes in. His apprentice, Serach, is studying quietly in a corner, half hidden among dolls in progress."

    show eilhart at right with dissolve


    e "So you made it. I was starting to get worried."

    e "I realize this isn't the most conventional meeting place, but please humor me."

    e "Why do you think I had you come here?"

    menu:
        "\"I'd say your guess is as good as mine, but you know why you brought me here.\"":
            $ eilhartAffinity = eilhartAffinity + 1

            l "I'd say your guess is as good as mine, but you know why you brought me here."

            l "I doubt it's for jubilant reasons, so why not just cut to the chase, hm?"

            "Luna tries not to look worried."

            l "(He can't know who I'm working for... Can he? There's no way anybody would know.)"

            l "(But I'd better not look nervous...)"

        "\"You have something to tell me about my investigation.\"":
            l "You have something to tell me about my investigation."
            "Eilhart chuckles a little, but the smile never reaches his eyes."
            e "Straight to the point, aren't you?"

    "Eilhart looks serious."
    e "I fear you've been a bit too aggressive in your digging around. Asking questions, no matter how discrete, never goes entirely unnoticed."

    e "Some of our colleagues... I'm sure you can guess which... are less than pleased by some of those questions."

    l "Are they now. What are you getting at?"

    e "I just came out of a meeting a few hours ago. They will be sending someone to tail you from now on."

    l "(Oh, snap. Not good.)"

    e "Look, I don't know what you're looking for, and it's your choice whether you're going to continue despite the spy or not, but..."

    e "Whatever it is, is it really worth risking your sister over this?"

    l "Risking her?"

    e "I'm afraid if you don't stop, we'll have another Nikolai on our hands..."

    menu:
        "\"Why would you warn me about this?\"":
            $ eilhartAffinity = eilhartAffinity + 1

            "Luna tries to look calm."
            l "I think that's blowing things out of proportion, don't you...?"

            l "I know my sister is innocent of anything they could accuse her of, and anything they could possibly come up with wouldn't lead to an extreme measure like that. Unless they plan on framing her, but can they really justify doing that to someone who isn't even in the Guild anymore?"

            l "I suppose the part that I should find most concerning, however, is that you'd warn me of this."

            "Eilhart smiles."
            e "I would be surprised if you didn't find it strange."

            e "I'm not stupid, Luna. Maybe a lot of it is my own fault, but I know I'm not exactly beloved by our \"esteemed colleagues\"."

            l "(...Pretty sure they would like you better if you didn't sound so sarcastic, Eilhart.)"

            e "Right now, the only reason I'm fine is because they have a common enemy. But if they take you down, it's gonna make them more confident, and there will be less opposition when they turn on me."

            e "And I know they will. In fact, more likely than not I'm the next target. So call it taking preventive action."

            l "Well I can't really argue with that. They've been apprehensive about you since the beginning..."

            e "Well, I suppose not many powerful, hard-working High Mages who descend from the great magical families of old appreciate having some random Joe go from nobody to the same rank as them."

            l "(Tell me about it. But it does make you wonder how he got into the Council...)"

        "\"Is that a threat?\"":
            $ eilhartAffinity = eilhartAffinity - 1

            l "Is that a threat?"

            e "Why you I threaten you?"

            e "I'm just saying, Luna. You get people in the Council upset asking questions about their affairs, and they start asking questions about yours."

            e "There's always something to be dug up. Even a necromancer like him probably wouldn't have been exposed if he kept to himself."

            l "(Is he saying Nikolai asked questions too? What kind of questions?)"


    e "In any case... You underestimate a High Mage's determination to keep their secrets safe."

    e "They didn't really approve of it, but framing her is the back-up plan. You know how influent some of us can be... how many favors are owed. Your sister really doesn't need this right now."

    l "(Really? He's telling it to my face, that they're going to frame her? They went and decided that in a meeting?)"

    l "(I can't tell if he's playing me, or if they're really that rotten...)"

    e "Won't you stop, Luna? While you still can?"

    l "(This sounds awfully familiar. But my answer is still the same.)"

    l "I can poke around with a little more finesse, but I can't promise I'll stop what I'm doing. I don't want to put Sola in a tough spot, even more now that she has Alice to worry about..."

    l "But I can't just sit by and do nothing. I've done far too much of that already."

    e "I can't talk you out of it, can I?"

    e "But there are so many that are more than content to just sit by and watch. What suddenly triggered this need of yours to risk your own family for this?"

    menu:
        "\"I'd tell you, but that would give you far more leverage than I'm comfortable with. Nice try though.\"":
            $ eilhartAffinity = eilhartAffinity + 1

            "Luna just smiles."

            l "I'd tell you, but that would give you far more leverage than I'm comfortable with. Nice try though."

            l "I've sat by and watched innocent people take heat for our mistakes one too many times, thank you. And I will not sit quietly if my sister has even the slightest chance at being one of them."

            e "(gives a mock sigh)\nOh, well. It was worth the try."
            e "In any case..."
            jump eilhart_question

        "\"I made a promise...\"":
            jump promise
    return

label promise:
    l "I made a promise..."

    e "Could you be any more vague? Who did you make this promise to?"

    menu:
        "\"As a matter of fact, yes. It wouldn't be fun if I told you, would it?\"":
            l "As a matter of fact, yes. It wouldn't be fun if I told you, would it?"

            e "Why tell me at all if you're just going to leave me curious?"

            e "Fine. So... What are you going to do with all of this?"
            jump eilhart_question

        "\"I met Dmitri Amarov.\"":
            $ toldEilhartAboutDmitri = True

            l "I met Dmitri Amarov."

            e "(stunned)\nWhat?! Nikolai's kid? How... Where?"

            l "In the demon realm. It turns out, he infiltrated the Guild and was under our noses all along."

            l "(It might be better not to tell him I was the one who helped him infiltrate us at this point...)"

            l "He was one of the apprentices that got left behind in the first expedition."

            "Eilhart raises a skeptic eyebrow."
            e "And he managed to survive in a place half a dozen High Mages couldn't?"

            l "He made friends with some demons."

            l "(...Better not say they were undead. Divines, I'm not helping convince anyone his father wasn't a necromancer, am I?)"

            l "Anyway... He told me Nikolai was framed. He wanted me to investigate the matter."

            l "(Well that caught his attention. Maybe too much?)"

            e "But the evidence was pretty convincing."

            l "You're the one who was just warning me that the Council wanted to get rid of me so badly they might frame my sister. You tell me if the evidence wasn't a little too convincing."

            e "Alright, I'll bite. Suppose you do find evidence that he was innocent..."
            jump eilhart_question
    return

label eilhart_question:
    l "(Wow. I've never seen him look so serious.)"

    e "What do you expect to do with all of this? Bring down the Council?"

    e "You know the problem isn't just one of us, but all of us. And even then it wouldn't keep innocent people from being hurt... Other rotten High Mages would just find their way in."

    menu:
        "\"I just want to convince everyone that not all High Mages are sell outs.\"":
            $ eilhartAffinity = eilhartAffinity + 1

            l "I honestly don't know what I plan on doing with the information. Perhaps simply convince everyone that not all High Mages are sell outs."

            l "All I know is that I've been quiet for too long, and I can't let things continue."

            e "You don't think all High Mages are sell outs?"

            l "(So you do?)"

        "\"I will bring down all of you if I have to.\"":
            $ eilhartAffinity = eilhartAffinity - 3

            $ threatenedToBringDownCouncil = True

            l "(I have to do this. I owe it to Nikolai...)"

            l "I will bring down all of you if I have to."

            l "I don't care if more rotten High Mages get in. I'll bring them down too."

            e "So you don't care about the damage you'll do?"

            l "(That look in his eyes... Did I make a mistake here?)"

            l "(But I've gone too far to back down now. Nikolai deserves better.)"

            l "Someone has to do it! The Council's corruption is an insult to the entire Guild!"

            e "I'd agree with you... But you know, as refreshing as your dedication is, people like that never last."

    #TODO play knocking sound
    "A knock intterupts them. Before Eilhart can say anything, a young, sickly-looking blonde boy shyly pokes his head inside the room."

    ek "Pop? Mom wants..."

    "Eilhart quickly cuts him off."
    e "What are you doing here? Didn't I tell you to keep out of the workshop?"

    "Luna does a double take."
    l "Wait what? \"Pop\"?"

    ek "S-Sorry. Mom asked me to ask you to buy some milk..."

    "The boy coughs quietly in the back of his throat."
    ek "Who's the lady?"

    e "She's from work. Now what did I say?"

    e "(glances at Serach)\nSerach, take him back to his mother."

    "Serach stands up and takes Erik's hand."
    se "Yes, sir."

    l "(Too late, Eilhart. There's no way I wouldn't notice this much dark energy.)"

    l "(Is this... A curse? A powerful one, too... What's going on here?)"

    if threatenedToBringDownCouncil and eilhartAffinity < 0:
        "The door opens discreetly as Serach comes back and stands quietly inside."

        l "(There's something off here. Eilhart looks tense... I don't like it. Maybe I shouldn't linger here.)"
        menu:
            "\"I didn't know you had a son.\" (Stay.)":
                jump serach_kills_luna

            "\"Uh... I'll be going.\" (Leave.)":
                l "Uh... I'll be going. See you at work."
                l "(Why do I feel like I'm running?)"
                jump meet_nikolai
    else:
        e "You were leaving?"

        menu:
            "\"Was.\" (Stay.)":
                l "Was."

                l "(But now I have some questions for you.)"

                l "I wasn't aware you had a son... not that I've ever delved into your personal life. He seems rather... under the weather. I don't suppose there's a reason for that, is there?"

                e "Well, yes, people not being aware of it was kind of the point."

                e "Children get colds. Which is why I wanted him in bed, not wandering around."

                l "(Really now.)"

                menu:
                    "\"Alright. I'll see you at work then.\" (Leave.)" :
                        l "(If he doesn't want to tell me, there's nothing I can do.)"
                        l "Alright. I'll see you at work then."
                        jump meet_nikolai

                    "\"Come on, I told you my secret.\"" if toldEilhartAboutDmitri == True:
                        l "Come on, I told you my secret."
                        e "...I guess you did."
                        jump eilhart_story

                    "\"How about a deal?\"" if toldEilhartAboutDmitri == False:
                        l "I'm not a sell out, Eilhart, you know that. Neither is my grandfather. Rather, he's feared this the whole time he's been on council."

                        l "I'm not saying we can save anyone... hell, I'm not even saying we can change it. But we can try, right? So I'll make you a deal."

                        l "You tell me what's up with him..."

                        l "And I'll tell you what I'm looking for, or who asked me to dig."
                        jump eilhart_story

            "\"Uhm... Yes.\" (Leave.)":
                l "Uhm...  Yes. See you later."
                jump meet_nikolai

        

    return


label serach_kills_luna:
    l "I wasn't aware you had a son... not that I've ever delved into your personal life. He seems rather... under the weather. I don't suppose there's a reason for that, is there?"

    e "(amused)\nMaybe, maybe not."

    "Eilhart suddenly becomes serious."

    e "Honestly, you don't really expect me to tell you, do you? Right after you threatened to bring down the same Council I happen to be part of?"

    l "(I have a really bad feeling--)"

    "There is movement behind Luna and something unseen traps her in a headlock."

    l "Ahh! Get--off--"

    "Luna lashes out with sharp shadow tendrils, but the strong arms around her neck keep choking her."

    l "(Impossible! How are they still standing?! How--)"

    "Light glints off the arms choking her. Underneath torn skin, there is only metal..."

    l "(An automaton?!)"

    l "Eilha--"

    e "Do it, Serach."

    l "Serach? Divines. His apprentice is an aut--"

    with tintred
    $ renpy.pause(0.5)

    "Serach snaps her neck. Luna goes limp in his arms."

    hide luna with easeoutbottom
    # show luna at Position(ypos = 1, yanchor = 0) with MoveTransition(0.5)

    "Eilhart's shoulders slump. He suddenly looks so very old and tired."

    # scene black
    # with Fade(0.1, 0.5, 0.5, color="#000")

    e "I don't disagree with you, Luna. The Council is rotten. Bringing it down would be a favor to everyone..."

    e "But I can't let someone who doesn't know how to hide her cards leave knowing about my family."

    e "I'm so, so sorry."

    e "Come, Serach. Let's hide her with the others..."

    scene black with fade

    $ renpy.pause(0.5)
    show text "Ending 1 of %d" % (numEndings) with dissolve

    $ renpy.pause()

    hide text with dissolve

    return





label eilhart_story:
    $ heardEilhartStory = True

    "Eilhart is silent for a long time."

    l "(He's really thinking it through, isn't he? This has to be something big...)"

    e "It was years ago. Back then, I didn't have the faintest how magic worked and I honestly didn't care. I just worked here and I was happy with it. It's been my family's business for as long as any of us can remember."

    l "(He looks wistful... Better days, I take it.)"

    e "There was some High Mage who was under investigation by the council. He was under fire for a great count of murders."

    l "(Murder? Years ago... I think Grandfather mentioned it. Was it Korone?)"

    e "When the investigation started closing in, he panicked and fled... He came into the city, and into our shop, and demanded that we hide him from the Guild or else he would kill us."

    e "We spent about three weeks like that. Then our food ran out, and he gave me permission to leave and go buy supplies. I had no intention of risking my family, but my wife... She was always so honest, so scrupulous."
    "Eilhart smiles sadly."
    e "While he wasn't listening, she insisted that I tell the Guild. So when I left, I went and warned them... They didn't really believe me, so they only sent a few mages back with me."

    l "They didn't send any High Mages? That's ridiculous. Even if they didn't believe you, they should have played it safe anyway."

    e "He killed them so easily. Then he turned on us... He cursed us. But I wasn't affected... You could say that was how I discovered my gift for magic."

    e "He didn't expect it. While he was still recovering, I put that thing over there..."
    "Eilhart motions towards a long, thin metal tool leaning against the wall."
    e "Right through his heart."

    e "But it wasn't enough to dispell the curse. I went to the Guild for help. I begged the Council to help find a cure... But do you think they did anything?"

    e "No, they didn't want to admit one of their own did that. So that they could keep up appearances, they even threatened us to shut us up. I'm fairly sure if I hadn't changed my identity after that, I wouldn't even be here now."

    l "I'm sorry... I had no idea."

    e "Do you see now why I have some trouble believing you when you say not all High Mages are sell outs?"

    l "I can't blame you."

    e "Maybe if you had been there back then, things would have been different."

    e "Or maybe you would have done nothing all the same, which makes you really no different from Lycioe or Victoria or any of them. 'Atoning' now won't make up for what not only me, but so many others have gone through."

    e "In any case, I joined the Guild hoping I could gain enough influence to force them to dispell the curse..."

    "Eilhart laughs wryly."
    e "I must have set some kind of record for blazing through the ranks like that, I was so desperate. When time is your enemy, nothing else matters, you know?"

    "His gaze falls."
    e "But I still wasn't fast enough. By the time I got to my post, it was too late. The curse has progressed too far, there is... There is no annulling it now."

    l "Eilhart..."

    e "My wife has been bedridden for the past few months, she doesn't have much long left. Erik isn't far behind, as you just saw... And our little Emma hasn't woken up since that day. Even if she did wake up, what's left of her body to live in? I just..."

    "Eilhart takes a deep breath, trying to calm himself."

    e "Needless to say, that is far, far more than I've told any of our colleagues, so I would appreciate some discretion."

    e "I went to insane lengths to keep my family's existence secret and keep them out of Council matters. So if you ever even think about threatening them or using them as leverage, I'm sticking that same tool through your heart too. Are we clear?"

    l "(He doesn't even look like he's kidding.)"

    e "Now tell me what it is you're looking for."

    l "I'm looking for the evidence used against Nikolai. I had started when his integrity was called into question, but stopped after I was too late. Now I'm looking again to see if I can trace it back."

    l "I want to know who framed him... and why. Nikolai didn't step on any toes that I was aware of. It doesn't add up."

    e "Are you that sure he really was framed? He could have had a life you didn't know of... Like I have a son, and not one of our colleagues ever imagined that."

    if toldEilhartAboutDmitri == True:
        l "Dmitri himself told me. Sure, you could say he was lying... But why ask me to look into it at all if he was?"

    else:
        l "That's different. I didn't think he was a necromancer back then... And I still don't, even now."
        l "(I can't really tell him Dmitri told me he was innocent...)"

    e "Given my story, I should be glad you're investigating... But even if some of the evidence might have looked shady, I thought a lot of it seemed genuine."

    e "If someone took it from our evidence vaults from previous cases, someone would have noticed, with all the noise surrounding the trial. Wouldn't only a real necromancer have access to the kind of equipment we found in his house?"

    e "Unless... Are you suggesting the one who framed Nikolai was the real necromancer?"

    l "The real necromancer perhaps, or someone who had access to alternate evidence. I don't really know, I haven't been able to dig that far."

    e "Well, it looks like you're going to have your work cut out for you. No one is exactly going to confess to being a necromancer."

    e "Good luck, Luna. And do watch your back, I'd really rather not be left alone with the rest of our \"esteemed colleagues\"."

    l "(laughs)\nIndeed, the last thing you need is to be left to the hounds. I'll do my best to be careful."

    l "(Well, this is a.... weird situation, to say the least. But now that we both have leverage against the other, it keeps both our secrets safe.)"

    l "(Unless one of us can strike faster than the other, my investigation should be safe with him...)"

    l "I'll see you at council then."

    e "See you."
    jump meet_nikolai
    return