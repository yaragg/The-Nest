# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define l = Character('Luna', color="#aa48ce")
define e = Character('Eilhart', color="#48ce7c")
define o = Character('Old man', color="#71684f")

define flash = Fade(0.1, 0.0, 0.5, color="#fff")


# The game starts here.
label start:
    $ eilhartAffinity = 0
    "Eilhart affinity is %(eilhartAffinity)d"
    jump luna_office_letter

    return
