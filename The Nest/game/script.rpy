# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image black = "#000"

# Declare characters used by this game.
define l = Character('Luna', color="#aa48ce")
define e = Character('Eilhart', color="#48ce7c")
define o = Character('Old man', color="#71684f")
define ek = Character('Erik', color="#4e6f4a")
define se = Character('Serach', color="#7f831f")

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define tintred = Fade(0.1, 0.2, 0.5, color="#f00")

# The game starts here.
label start:
    $ numEndings = 1
    $ eilhartAffinity = 0
    $ toldEilhartAboutDmitri = False
    $ threatenedToBringDownCouncil = False
    $ heardEilhartStory = False
    "Eilhart affinity is %(eilhartAffinity)d"
    jump luna_office_letter

    return
