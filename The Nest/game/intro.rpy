label intro:
    scene black
    "Being made part of the High Council is cause for celebration."

    "There are only ever a dozen or so High Mages at a time, and for good reason. Together, the Council governs the Mages' Guild and by extension everywhere the Guild has dealings with."

    "But Luna's grandfather Readak, upon learning of the news, simply laughed that odd, cackling laugh of his."

    "A High Mage himself, she thought he looked a little sad."

    r "Welcome to the viper's nest."

    "It took only two months before she learned what he'd meant. When she told him that much, he simply cackled again."

    "In truth, it would be years before she fully understood how deep that pit could go."

    "By then, she had just returned from a long mission in an unknown realm..."

    jump council_exposition
    
    return


label council_exposition:
    play music "sound/bgm/Sketchy Logic - Shop of the Arcane.mp3" fadeout 0.7 fadein 0.5
    scene council_room with fade

    show albert flip at left with dissolve

    a "Luna, Emil. Believe me when I say it's good to see you two."

    "Yet the apparent relief of meeting them after years of absence is overshadowed by a grim frown in High Mage Lycioe's face."

    "It is easy to understand why:"

    a "What happened to the others...?"

    "They had been part of the second group, tasked with bringing back the missing members from the first expedition."

    "Out of six High Mages in their group sent to explore the land beyond that mysterious, unexplained portal in the middle of the sea, only three returned--and that after six years of unexplained absence."

    "None of the apprentices they had set out to rescue made it back."

    "Add to that the two missing High Mages from that first failed expedition, and the Council has lost half of its members."

    show emil at Position(xpos = 0.65, xanchor = 0.5) with dissolve

    show luna flip at Position(xpos = 0.8, xanchor = 0.5) with dissolve

    "Luna and Emil exchange glances. They had already agreed on what to tell their peers before they crossed back into the human realm, but it doesn't make the weight any easier to bear."

    "There is too much to hide."


    l "It's a dangerous realm, that's all I can say. Elrek just vanished, he warped away and we never heard from him again."

    l "Lester was killed by the vampires..."

    l "(True, if you consider that he's one of them now. Undead is still dead, right?)"

    "Albert looks saddened."

    a "Killed by the creatures he hated most, huh... What of Crowe? He must have been devastated."

    "Necromancy and anything to do with undeath have long been outlawed by the Guild, punishable by burning at the stake."

    "That is why Luna keeps up the lie:"

    l "He didn't have much time to grieve. They got him, too."

    l "(Let's just keep it at that.)"

    e "What about the apprentices?"

    l "We never found them."

    "Emil gives Luna a sidelong glance. Nevertheless, he backs her version:"

    em "Honestly, given how easily Lester and Crowe went down, it's anyone's guess how long a group of apprentices would last."

    em "They were probably gone long before we ever set out to rescue them..."

    "There is a moment of silence as the council takes the grim news in. Finally, Albert awkwardly clears his throat."

    a "You told us about the others. But what about you two?"

    e "Right. You've been gone for what, six years? That's one hell of a sabbatical."

    "Emil clenches his left fist so hard the metal groans. His tone is sharp as a blade."

    em "I was in a cell for five years. Does that answer your question?"

    "Emil losing his cool is enough to surprise anyone in the Council, but stunned murmurs follow his words."

    a "What... Why?"

    em "(bitterly)\nVampires."

    l "They were afraid of his magic. And for good reason, it's how he got us out of there."

    "The power to control those who have wronged him, and the curse to be compelled to obey those he wrongs. A fearsome magic no one could quite explain--the perfect excuse for their miraculous escape."

    "And so continues the meeting. All full of excuses, and Luna fears she wouldn't keep all the lies straight if it weren't for Emil's help..."

    jump emil_office
    return


label emil_office:

    scene emil_office with fade

    "Luna breathes a sigh of relief."

    show luna at left with dissolve
    show emil at right with dissolve

    l "I never want to do that again."

    em "(smiling wryly)\nWhat, the part where we lied to the Council's face? Wait, that's the entire meeting."

    l "Thank the Divines you were there. I swear, I don't know how you do it, I was about to break in cold sweat."

    em "(smiles a little)\nYou know the deal. Live long enough with my magic..."

    "Emil shakes his head."

    em "But Luna, this is a dangerous game you've got us playing. I get lying about Crowe..."

    em "But Dmitri kept me in that cell for five years, Luna. Why didn't you tell them?"

    l "Emil..."

    l "You know why. It was his condition for letting us go."

    l "I have to find out what happened to Nikolai... He was no necromancer."

    em "Luna. Think about it. If what Dmitri said is true... If Nikolai was framed..."

    l "Then it's my job to clear his name!"

    em "It isn't!"

    em "It's been almost twenty years. For the Divines' sake, Luna, the man is dead, his son is safe in another realm entirely and no one can ever get to him with the vampires protecting him."

    em "What more do you want? I know you cared about him..."

    "Emil looks away to hide the jealousy they both know is there."

    em "But if it's true that he was framed, then someone in the Council had a problem with him. And that someone might still be here."

    em "You just got back. Your sister got kicked out of the council because she had Lester's kid. Is it really worth risking it all for something that happened two decades ago?"

    "Emil pauses and his eyes soften as he looks back at Luna."

    show emil at Position(xpos = 0.72, xanchor = 0.5) with MoveTransition(0.2)

    em "Please. I don't want to see you hurt..."

    l "Emil..."

    l "I made a promise. I'm the only person Dmitri has left..."

    em "That's not true. He's got his own family now. Please, Luna. You're going to get yourself killed."

    l "I failed him once. I failed both of them. I couldn't defend Nikolai..."

    l "And I couldn't raise that little boy who had no one else to look to. Now all he wants is answers. How can I deny him that, Emil?"

    l "This isn't the kind of Council I want to be part of..."

    "Emil hesitates for a long moment."

    em "Then at least play it safe. Don't go around making enemies."

    l "I have no wish to. But please, if you're worried, help me. I know I can do so much better if you have my back."

    "Emil looks pained."

    l "(Whenever we get close you push me away, but then you act like this... What am I supposed to think, Emil?)"

    em "I want to. Divines, you know I do."

    em "But if I make any false accusations, it's only going to get my magic turned against us."

    em "You're going to be in enough trouble without that..."

    em "I can't speak out, but I can still give you advice. Come to me before you do anything rash... Okay?"

    l "Will do. I'm sorry to put you in this position."

    "Emil smiles and gives a mock bow."

    em "Anything for you, milady."

    jump luna_office_letter

    return