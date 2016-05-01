label luna_office_letter:
    "Luna is hard at work reviewing evidence."

    #TODO Play knocking sound

    with flash
    "Luna jumps in surprise and scramble to hide her papers."

    l "Come in."

    #TODO play paper rustle sound

    "A note is slid out from underneath her door. Luna frowns as she picks it up."

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
    
    "Luna looks around the shop, impressed with the realism of the dolls displayed."

    l "I would buy one for Alice if they weren't so creepy..."

    "Luna walks up to the counter and hands the ad over to the old man working there."

    l "This found its way into my office."

    "The old man smiles."

    o "He's waiting in the workshop."

    l "(He...? Well, let's see who this secret admirer is...)"

    #TODO show Eilhart's workshop

    "Eilhart is hunched over a table working on a doll, and straightens back up to look at Luna as she comes in. His apprentice, Serach, is studying quietly in a corner, half hidden among dolls in progress."

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

    # if threatenedToBringDownCouncil and eilhartAffinity <= 0:

    #     "The door opens discreetly as Serach comes back and stands quietly inside."

    #     l "(There's something off here. Eilhart looks tense... I don't like it. Maybe I shouldn't linger here.)"
    # else:

    return