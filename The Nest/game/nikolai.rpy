label meet_nikolai:
    scene nikolai_house with fade
    $ renpy.pause(0.5)

    show luna at left with moveinleft

    #TODO play sound of wind howling

    $ renpy.pause(0.5)

    show luna flip at left with dissolve
    l "Looks like I lost my tail... Good."

    show luna at left with dissolve
    l "It's been abandoned for so long... Dmitri was too young to live here and no one wanted to live in a necromancer's house."
    l "If there's anything left from all those years ago, this is the place to find it..."

    hide luna

    show nikolai_house_int with fade
    show luna at left with dissolve

    "The furniture and everything it once held have been left to rot in the empty house. Its only inhabitants are insects and a pack of rats, and one stops and stands up on its hind legs, sniffing at Luna and peering at her with beady black eyes."

    "It scampers off and squeaks as it slips on a thin layer of ice, then quickly gets back up and scurries off somewhere unseen."

    l "I still remember this house... Oh Dmitri, do you remember it the same way?"

    l "(Did you, too, wish you could stay in this house forever...?)"

    show luna at left with vpunch

    "Luna almost slips on the same patch of ice. She scowls, then confusion comes over her face."

    l "Wait... How did ice get here?"

    "A loud creak from farther away makes Luna jump. She turns and sees boot marks on the dusty floor."

    ##TODO play loud creaking sound

    "Luna's hair stands on end."
    l "(laughing nervously)\nOh dear. This is the stuff horror stories are made of."

    l "Of course dark magic exists... It's what our Guild is supposed to protect people against."

    l "But there would be no such magic in your house, right, Nikolai...?"

    "Luna takes a deep breath to steel herself, then slowly moves to the source of the noise, hands swirling with magic."

    scene nikolai_study with fade
    show luna at left with dissolve

    "A hooded figure slowly stands up from where it was crouched behind the desk and faces Luna."

    #TODO increase howling wind sound

    l "Wha--"

    #TODO play window shattering sound

    with blueflash

    "One of the windows shatters and the wind sends papers fluttering all across the room. An inkwell falls and shatters loudly."

    l "Gyaah!"

    l "What... Who are you?"

    l "(It doesn't feel human. It can't be one of Eilhart's automatons... They're not that lifelike yet... Are they?)"

    l "(Is that... Frost near its feet?)"

    l "(Wait... Snow inside the house?! How can it be?)"

    #TODO make wind even louder

    u "Why are you here?"

    u "Why now?"

    "Luna flinches, then shouts trying to be heard above the wind."
    l "I... I'm not here simply for my own sake!"

    l "I come as much for Dmitri Amarov as I do for myself! I'm just looking for answers as to what happened here... I don't feel that Nikolai's case was examined enough. I want to know if he was innocent... and if he was, why he was framed!"

    l "(I don't know what this is about... But what else can I say?!)"

    "The wind dies a little."
    #TODO make wind quieter

    u "You had years for that! Why only now?"

    l "I'm finishing what I started."

    l "I started investigating Nikolai's case when he was charged, but everything I came across either disappeared or led me to a dead end."

    l "I didn't try hard enough and he died because of that. So when Dmitri asked if I would look again... I agreed."

    l "I want to put this to rest once and for all. I want to know the truth. People need to know if the Guild condemned an innocent man."

    l "(And I'm almost certain that's the case...)"

    "The wind stops, but the room is still freezing."

    u "And what if that is the case? What will you do if the Guild murdered an innocent man...?"

    u "How far are you willing to go for this, Luna?"

    l "(How does it know my name?)"

    l "I'm willing to go as far as it takes. I failed the Amarov family once... I refuse to do it again."

    "The figure is silent for a while, then motions to the floor where he'd been crouched."
    u "Break the seal. It was not made for a dead man to open."

    show luna at right with MoveTransition(1.2)
    $ renpy.pause(0.7)

    l "A rune...?"

    "The figure takes down its hood, revealing a face made entirely of ice."

    u "You didn't fail us... I know you kept fighting until the end."

    show luna flip at right with dissolve

    "Luna breaks the seal and straightens back up. Her face softens, eyes a painful combination of confusion, sadness and the tiniest bit of happiness."

    l "Nikolai... So it is you. How...?"

    n "I don't know. I just... Woke up, and I was there. It was only a few years ago. I'd been dead for at least a decade. I can't even begin to explain it..."

    l "I missed you. I missed you so much."

    "Nikolai looks away."
    n "I know."

    "Not knowing how to react, Nikolai motions awkwardly at the seal."
    n "I can imagine why someone would want me dead, but I have no idea who."

    "Nikolai moves over to the hidden cache and pulls out a few glass spheres from behind a stack of papers."

    l "Recording spheres...?"

    "Nikolai holds up a sphere and it glows before two voices fill the room. His own, and a familiar one..."

    jump recording


    return

label recording:
    c "Why are you recording this, Nikolai?"

    nr "For security. In case anything happens. You should, too."

    c "Do you really think something will happen?"

    nr "I don't know, but I'm not taking the chance. You know the company we keep can be... dangerous."

    nr "I owe it to Dmitri to be careful... And if that's not enough, to at least leave him something to understand why."

    c "You do realize I'm a time mage?"

    nr "Yes, but so do the people we're investigating. Now..."

    nr "This is week 10 of our investigation. So far, we've found 24 possible victims among the people who went missing in the town of Ayla and surroundings."

    nr "They were always people who left town alone, and always very healthy. There seems to be a predominance of light hair and eyes, although the last ones were more varied. Ages vary as well, although most were 26 and younger."

    nr "Of these 24 people, 18 had magical blood and 11 were affiliated to the Guild in some way."

    nr "Though there is nothing physical to suggest the same person is responsible, kidnappings of magically inclined people are relatively rare and this represents a considerable increase in statistics."

    l "What...? What is this?"

    nr "Furthermore, one of these was a Senior Spellcaster, and although retired, he was believed to be still very powerful. In order to subdue him, one would have to be just as powerful and thus likely in the higher ranks of our Guild."

    nr "The 15 missing corpses from the same area would also suggest Necromancy might be involved, although we cannot be sure at this time if it was the same person."

    nr "This covert investigation was requested by the Aylan branch of the Guild. Any clues the local investigators have found either led nowhere or were disposed of with suspicious readiness."

    nr "Whether it is a powerful necromancer out there, or a high-ranked mage in our own midst, our purpose is to determine whether someone within the Council would have means and motive to do this..."

    jump crowe_discussion

    return

label crowe_discussion:
    l "What... I never heard of any of this. A covert investigation into the Council itself...?"

    l "(No wonder someone would want to frame him. But why didn't Crowe come forward with this if he was investigating it too? Wait...)"

    l "(Oh, crap.)"

    l "Nikolai... Crowe is a necromancer. We found that out the hard way in our expedition."

    l "(Though he did help us with the vampires...)"

    l "He would have had the means to frame you. He had access to the materials that would have been needed."

    l "It was all so meticulously planned... Almost none of the artifacts are out of place or traceable. It's very, very possible some of the relics were created by whoever planted the evidence."

    n "He what?!"

    with blueflash

    "Another window shatters, making Luna jump."

    n "Wonderful. I've been working with the biggest hypocrite in this world, and in the next realm as well. Helping chase a potential necromancer... Keeping quiet while I was accused."

    n "Or, if what you say is right, framing me in the first place."

    "The room temperature has dropped considerably, and Luna shivers in the cold."

    l "Well he would have had access to the right kind of materials. I've been hunting down similar pieces and some of them weren't easy to come by. I think it's safe to assume that whoever did this practiced the art, or knew someone who did."

    if heardEilhartStory == True:

        l "But..."

        l "(Light hair and eyes? And the culprit had to have immense magic...)"

        l "Could it be...? Eilhart?"

        n "What about him?"

        l "Well... Before he became a High Mage, his family fell victim to Korone. All of them were stricken with powerful ailments, and by the time he made it high enough to break the curse, there was no going back on it."

        l "(Sorry, Eilhart. But if you're involved in this, I can't really keep your secret from him...)"

        l "It's not... impossible to assume he's been using his automatons to try and bring his family back, and there's a good chance he'd need to know necromancy to do so."

        "Nikolai looks surprised."

        n "Eilhart... Really? I never would have guessed. Still... You may be right. When I got here a few weeks ago, it was clear someone was in the house before. It could have been him."

        n "I'm not sure how the automatons would help, but if he can animate matter and give it will, I suppose he might think he could animate bodies as well... And that, indeed, is Necromancy."

        n "But then why kidnap all those people? You think they were sacrifices, or practice? He could have just stuck to the corpses he was stealing from the graveyards... No need to kill, unless it was part of some ritual."

        "Nikolai gives a wry smile."
        n "Contrary to popular belief, I really wouldn't know."

        l "Sadly I know about as much as you. Perhaps Dmitri would have a better idea. I know he's been struggling with this puzzle just as much as I have..."

    else:

        n "We need answers. What became of Crowe?"

        l "He was one of those that joined the demon High King. The vampires Dmitri is living with can likely summon him, but it doesn't mean we'll get any answers."

        n "He's not in the Guild anymore. He's got nothing to lose. The least he could do is come clean."

        l "I know. And I will badger him until he does, I promise. But honestly..."

        n "What?"

        l "I'm not sure about this, Nikolai. By \"exposing\" you as a necromancer, he would just be making the Council be even more careful about necromancers hidden in our midst. This would be bad for him."

        n "You think he didn't do it?"

        l "He's the most obvious suspect, yes, but as far as the Council is concerned, so were you."

        l "Maybe this isn't as straightforward as we'd like to think. He could have had an accomplice, if it was him at all... The Council DOES seem a little too concerned with where I stick my nose."

        "Luna hesitates for a moment, then looks at Nikolai again."
        l "I could send word to Dmitri, see if he can contact Crowe in the meantime. I know he's been struggling with this puzzle as much as I have..."

    n "Dmitri..."

    "Luna smiles softly."

    l "He found himself a vampire woman and settled down, would you believe it? He has a little one of his own now."

    l "A sweet four year old by the name of Lucille. She's very articulate... It makes me think of you."

    "Nikolai smiles at the news, but still looks so very sad."

    l "What is it? You look troubled."

    n "Send him the recordings if you wish. But... Please don't tell him how you got them."

    l "What? Why?"

    n "You said it yourself. He has a family of his own now... I was never much of a father in life, how fair would it be to disrupt his life now that I'm dead?"

    n "I don't even know how I came back. That also means I don't know how long this will last. For all I know, I could just disappear tomorrow, for good this time."

    n "I don't want to put him through that once again."

    l "Nikolai..."

    menu:
        "\"I will respect your wishes.\"":
            l "I can see why you would want that. I wish you would come back to him, but... I will respect your wishes."

            n "(smiling sadly)\nThank you, Luna. Believe me, I wish I could..."
            jump find_sphere

        "\"Stop being a coward.\"":
            l "Stop being a coward."

            n "What?"

            l "He's your son. He might not be a little boy half your size anymore, but he still needs you."

            l "If you weren't enough of a father in life... Then now is the time to try again."

            l "You were given a second chance, Nikolai. Not many get that opportunity. Don't waste it... Please."

            "Nikolai hesitates but nods, still a little flustered."
            n "I... I see. I will... Think about it."

            n "I'm sorry if I upset you. Maybe you do have a point. I just... I guess I'm afraid."
            jump find_sphere
    return


label find_sphere:

    "Luna pauses for a moment, then hugs Nikolai tightly despite shivering with the cold."

    l "I won't let you down... Not after you've lost so much already. I won't let them take any more from you."

    "Nikolai opens his mouth to say something, but stops."

    "Flustered, he pulls away from Luna."

    n "I... Thank you. Nobody else should have to go through this. To make sure it never happens again... That is the best I could hope for."

    "Nikolai suddenly pauses and frowns, looking around."

    n "Do you feel it?"

    l "(Wow, Nikolai. Talk about a smooth way to change the subject.)"

    "Nikolai catches the way she's looking at him and scowls, still flustered."
    n "I mean it. Over there."

    "Giving in, Luna goes over to the bookshelf he's pointing at and pushes the books aside. She gasps at the sight of a small, softly glowing glass sphere."

    l "A recording sphere?!"

    n "What?! Let me see!"

    n "This doesn't make sense. Who...? Wait."

    l "It's so smooth... Too smooth. You could almost say it's impossibly perfect."

    "Nikolai frowns, suddenly understanding where she's going."

    n "An object not of this world. Not naturally in it, in any case. Are you thinking...?"

    "Luna nods and easily completes his sentence."
    l "There's only one man that could make something like this. A creation mage... The most skilled one that we know of."

    n "Albert Lycioe."

    l "But why would he hide a recording sphere here? It doesn't make sense."

    n "Unless he figured out what you were investigating and was afraid of what you might find out."

    "Luna is quiet for a moment, fiddling with the sphere as she tries to get it to play its recording."

    l "Damn, I can't get it to play. It's warded against outside interference. It would take a better enchanter than I to break Albert's charm."

    l "Maybe I should just go confront him. He can't really deny it's his work, I doubt his ego could take people thinking there's someone as skilled as him out there."

    l "(Wait. I do know an enchanter that's more than powerful enough to break through this...)"

    l "(Should I go to Eilhart? At least I could find out what this sphere recorded before I do anything about it...)"

    menu:
        "Confront Albert about the sphere.":
            if heardEilhartStory == True:

                l "(Eilhart is starting to look like a really good suspect... I don't know what Albert is up to, but going straight to our prime suspect sounds like a terrible idea.)"

                l "(Besides, if he sees the recording he'll know Nikolai is around. I'd better go to the source instead...)"

                l "Looks like it's time to pay one pompous redhead a visit."
                jump albert_study

            else:

                l "(Eilhart is too unpredictable. I don't know what he'd do if he saw Nikolai on the recording. I'd better go to the source instead...)"

                l "Looks like it's time to pay one pompous redhead a visit."

                jump albert_study

        "Ask Eilhart for help viewing the recording.":
            "THIS PATH NOT IMPLEMENTED FOR NOW"


    return