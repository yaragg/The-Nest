label albert_study:
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