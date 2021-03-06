# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image black = "#000"

# image luna = "Luna.png"

image luna flip = im.Flip("Luna.png", horizontal=True)
image albert flip = im.Flip("Albert.png", horizontal=True)
image emil flip = im.Flip("Emil.png", horizontal=True)

# Declare characters used by this game.
define l = Character('Luna Dieinoche', color="#aa48ce")
define e = Character('Eliphas Eilhart', color="#48ce7c")
define o = Character('Old man', color="#71684f")
define ek = Character('Erik', color="#4e6f4a")
define se = Character('Serach', color="#7f831f")
define n = Character('Nikolai Amarov', color="#2153b4")
define u = Character('???', color="#2153b4")
define nr = Character('Nikolai Amarov (recording)', color="#2153b4")
define c = Character('Hector Crowe (recording)', color="#979ba5")
define a = Character('Albert Lycioe', color="#b20916")
define v = Character('Victoria Reese', color="#d6700c")
define ca = Character('Caers', color="#a012a0")
define r = Character('Readak Dieinoche', color="#bfb31a")
define ve = Character('Vera Lycioe', color="#b20916")
define s = Character('Sola Dieinoche', color="#cec22b")
define alc = Character('Alice', color="#e8f464")
define em = Character('Emil Morato', color="#6a9af7")


define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define tintred = Fade(0.1, 0.2, 0.5, color="#f00")
define blueflash = Fade(0.1, 0.0, 0.5, color="#00f")
define longfade = Fade(2.0, 0.0, 0.5, color="#000")

define right = Position(xpos = 0.75, xanchor = 0.5)
define left = Position(xpos = 0.23, xanchor = 0.5)

# The game starts here.
label start:
    $ numEndings = 5
    $ eilhartAffinity = 0
    $ toldEilhartAboutDmitri = False
    $ threatenedToBringDownCouncil = False
    $ heardEilhartStory = False
    $ eilhartKeptSphere = False
    # "Eilhart affinity is %(eilhartAffinity)d"
    jump intro

    return
