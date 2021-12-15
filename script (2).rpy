# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("KING 11")
define e = Character("Knight")
define r = Character("siblor")
define s = Character("Shark")
define b = Character("Beer")
define z = Character("yanglob")
define x = Character("Demon lord")
define d = Character("develop")
define empty = Character("")
define die = 0


label start:
    stop music
    play music "audio/castle.mp3"
    scene racha1
    show invisible
    k "Hello my knight"

    k "You have a new mission"
    scene racha2
    show invisible
    with fade

    k "You must go kill the Demon Lord"

    k "I have prepared a weapon for you"

    scene racha3
    show invisible
    with fade

    k "Go on, go kill it"

    scene weaponroom
    with fade

    e "Choose your weapon"

    menu:
        "sword":
            jump bg1
        "gun":
            jump bg2
        "book":
            jump bg3
        "pokeball":
            jump bg4
    label bg1:
        scene sword
        show invisible
        with fade
        play sound "audio/sword.mp3"
        e "Good"

        scene door
        show invisible
        with fade
        play music "audio/land.mp3"
        empty "Front door"

        menu:
            "Parachute":
                jump car
            "motorbike":
                jump motorbike
            "taxi":
                jump taxi
            "walk":
                jump walk

        label car:
            scene parachute1
            show invisible
            with fade
            play sound "audio/air.mp3"
            e "You got parachute"
            scene parachute1
            show invisible
            with fade
            e "JUMP!!!"
            scene parachute2
            show invisible
            with fade
            e "UMM"
            scene parachute3
            show invisible
            with fade
            e "ARGH!!!"
            scene parachute4
            show invisible
            with fade
            e "Open parachutee"
            scene parachute5
            show invisible
            with fade
            e "You choose the wrong one"
            e "OH SHIT"
            scene parachute6
            show invisible
            with fade
            play sound "audio/smash.mp3"
            e "ARKKKK!!!"
            jump died
        label motorbike:
            scene motorbike1
            show invisible
            with fade
            play sound "audio/Gan.mp3"
            e "WOW THAT SO COOL!!"
            scene motorbike2
            show invisible
            with fade
            e "ngan ngan"
            scene motorbike3
            show invisible
            with fade
            play sound "audio/smash.mp3"
            r "Go to fucking hell, you're trash"
            jump died
        label taxi:
            play music "audio/initiald.mp3"
            scene taxi1
            show invisible
            with fade
            e "Taxi please"
            scene taxido1
            show invisible
            with fade
            e "ngan ngan"
            scene taxido2
            show invisible
            with fade
            e "Good luck bro"
            stop music
            scene moutain
            play music "audio/land.mp3"
            show invisible
            with fade
            e "Moutain"

            menu:
                "waterfall":
                    jump waterfall
                "climb":
                    jump climb

            label waterfall:
                scene moutain
                show invisible
                with fade
                e "Water"
                menu:
                    "swim":
                        jump swim1
                    "walk":
                        jump walkwaterfall
                label swim1:
                    play sound "audio/waterfall.mp3"
                    scene swim1
                    show invisible
                    with fade
                    e "You see waterfall"
                    scene swim2
                    show invisible
                    with fade
                    e "You jump"
                    scene swim3
                    show invisible
                    with fade
                    play sound "audio/toom.mp3"
                    e "Toom!!!"
                    play sound "audio/waterfall.mp3"
                    scene swim4
                    show invisible
                    with fade
                    e "print(Hello fish)"
                    scene swim5
                    show invisible
                    with fade
                    s "ngam ngam ngam"
                    s "this is so delicious, thank you daddy"
                    jump died
                label walkwaterfall:
                    play sound "audio/waterfall.mp3"
                    scene walkwaterfall1
                    show invisible
                    with fade
                    e "Walk"
                    scene walkwaterfall2
                    show invisible
                    with fade
                    stop sound
                    play music "audio/monbattle.mp3"
                    e "You found Mini Cyclop"
                    scene walkwaterfall3
                    show invisible
                    with fade
                    e "That so noob, fight me"
                    scene walkwaterfall4
                    show invisible
                    with fade
                    e "ngang nagnag!!!"
                    e "What?"
                    scene walkwaterfall5
                    show invisible
                    with fade
                    e "..."
                    scene walkwaterfall6
                    show invisible
                    with fade
                    e "This is not good"
                    scene walkwaterfall7
                    show invisible
                    with fade
                    e "I'm sorry, just kidding"
                    scene walkwaterfall8
                    show invisible
                    with fade
                    play sound "audio/smash.mp3"
                    e "ARkkk!!!"
                    jump died
            label climb:
                scene moutain
                show invisible
                with fade
                e "climb this moutain"
                e "How do I climb this?"
                e "Choose your climbing method"

                menu:
                    "your hand":
                        jump hand
                    "suction cup":
                        jump suctioncup

                label hand:
                    scene hand1
                    show invisible
                    with fade
                    e "you trying to climb by hand"
                    scene hand2
                    show invisible
                    with fade
                    e "hueb hueb"
                    scene hand3
                    show invisible
                    with fade
                    e "Reach the top of the mountain"
                    scene hand4
                    show invisible
                    with fade
                    e "CRACK!!!"
                    e "ARGHH!!!!!"
                    scene hand5
                    show invisible
                    with fade
                    e "NOOOOOOOO"
                    scene hand6
                    show invisible
                    with fade
                    play sound "audio/smash.mp3"
                    e "ACKKKK!!!!!"
                    scene hand7
                    show invisible
                    with fade
                    e "Still fortunately not dead"
                    scene hand8
                    show invisible
                    with fade
                    play sound "audio/smash.mp3"
                    e "TOOM!!!"
                    e "ARGHH!!"
                    jump died
                label suctioncup:
                    scene suction cup1
                    show invisible
                    with fade
                    e "you choose suctioncup"
                    scene suctioncup2
                    show invisible
                    with fade
                    e "pump pump pump"
                    scene suctioncup3
                    show invisible
                    with fade
                    e "Reach the top of the mountain"
                    scene suctioncup4
                    show invisible
                    with fade
                    e "CRACK!!!"
                    e "ARGHH!!!!!"
                    scene suctioncup5
                    show invisible
                    with fade
                    e "You jump out"
                    scene suctioncup6
                    show invisible
                    with fade
                    e "้almost died"
                    e "Let's climb"
                    scene suctioncup7
                    show invisible
                    with fade
                    e "Finally"
                scene castle
                show invisible
                with fade
                play music "audio/dunmu.mp3"
                empty "castle"

                menu:
                    "basement":
                        jump basement
                    "floor":
                        jump floor

                label basement:
                    scene beer1
                    show invisible
                    with fade
                    play music "audio/monbattle.mp3"
                    e "you found beer monster"

                    scene beer2
                    show invisible
                    with fade
                    e "choose your way"
                    menu:
                        "fight":
                            jump beerfight
                        "run":
                            jump beerrun

                    label beerfight:
                        scene beerfight1
                        show invisible
                        with fade
                        e"you wanna fight beer"
                        e"Hiyaaa"
                        b"HA HA HA"

                        scene beerfight2
                        show invisible
                        with fade
                        play sound "audio/smash.mp3"
                        e"you died"
                        b"so bored"
                        b"noob"
                        jump died
                    label beerrun:
                        scene beerrun1
                        show invisible
                        with fade
                        e"you run"
                        b"WHATT!!!"

                        scene beerrun2
                        show invisible
                        with fade
                        b"HEY"
                        b"STOP NOOB STOP"

                        scene beerrun3
                        show invisible
                        with fade
                        B"Arr"

                        scene beerrun4
                        show invisible
                        with fade
                        B"TOOM!!!"

                        scene beerrun5
                        show invisible
                        with fade
                        e"you win without doing anything"
                        jump bossroom
                label floor:
                    scene rub1
                    show invisible
                    with fade
                    e "You found yanglobman"

                    menu:
                        "fight":
                            jump yanglobfight
                        "run":
                            jump yanglobrun

                    label yanglobfight:
                        scene rubfight1
                        show invisible
                        with fade
                        play music "audio/monbattle.mp3"
                        e"You choose fight"
                        e"Hiyaaa!"
                        z"Great"

                        scene rubfight2
                        show invisible
                        with fade
                        z"ZUAB!!"

                        scene rubfight3
                        show invisible
                        with fade
                        z"DELETE"
                        e"my body delete argh"
                        e"I won't give up"

                        scene rubfight4
                        show invisible
                        with fade
                        e"ZUAB"
                        e"HIYAAA"

                        scene rubfight5
                        show invisible
                        with fade
                        e"KRUEDDDDD!!!!"

                        scene rubfight6
                        show invisible
                        with fade
                        play sound "audio/smash.mp3"
                        e"HIYAAAA!!!!"
                        z"ARk!"

                        scene rubfight7
                        show invisible
                        with fade
                        z"You win"
                        z"I will return what I deleted"
                        z"You is Romantic boy"
                        z"You should choose  you way"
                        z"go that my bossroom way"
                        e"thank that fight so good"
                        z"Phoo "
                        jump bossroom

                    label yanglobrun:
                        scene rubrun1
                        show invisible
                        with fade
                        e"You choose run"

                        scene rubrun2
                        show invisible
                        with fade
                        z"Hmmm"
                        z"You not romantic"

                        scene rubrun3
                        show invisible
                        with fade
                        z"Jump"

                        scene rubrun4
                        show invisible
                        with fade
                        e"argh that so fast"

                        scene rubrun5
                        show invisible
                        with fade
                        play sound "audio/smash.mp3"
                        e"Argh! what mybody delete"
                        z"deleted"

                        scene rubrun6
                        show invisible
                        with fade
                        z"You are not man"
                        z"you lost romantic"
                        z"you not brave"
                        z"Unworthy of being in this world"
                        z"Phoo"
                        jump died
                    label bossroom:
                        scene bossroom1
                        show invisible
                        with fade
                        play music "audio/bossfight.mp3"
                        e"DEMON LORD ROOM"
                        e"finally"
                        e"Must kill you for the peace of this city."

                        scene bossroom2
                        show invisible
                        with fade
                        e"Skill"
                        e"BUFF Attack"
                        e"ATK UP"

                        scene bossroom3
                        show invisible
                        with fade
                        e"HIIIII!!!"

                        scene bossroom6
                        show invisible
                        with fade
                        e"YA!!!!"
                        x"chueb"

                        scene bossroom7
                        show invisible
                        with fade
                        e"where he go"
                        x"you back"
                        scene bossroom8
                        show invisible
                        with fade
                        x"Are you ready to die yet?"

                        scene bossroom9
                        show invisible
                        with fade
                        x"SWING!!!"
                        e"Arghh!!!"

                        scene bossroom10
                        show invisible
                        with fade
                        e"Arghh that so fast!"

                        scene bossroom11
                        show invisible
                        with fade
                        e"Hiyaa!!!"
                        e"Use Sword SKILL"

                        scene bossroom12
                        show invisible
                        with fade
                        e"Sword of FIREER GOD SPEED!!!!"

                        scene bossroom13
                        show invisible
                        with fade
                        e"Boom!"
                        e"Faster than"

                        scene bossroom14
                        show invisible
                        with fade
                        e"Boom!"
                        e"FASTER FASTERRR!!!"

                        scene bossroom15
                        show invisible
                        with fade
                        e"Boom!"
                        e"YAAA!!!!"

                        scene bossroom16
                        show invisible
                        with fade
                        e"ARGHH"
                        e"My arm"
                        e"I not have enegy to standup"

                        scene bossroom18
                        show invisible
                        with fade
                        x"USELESS"
                        x"You stronger"
                        x"it not than me"
                        x"i want to talk to you"
                        x"How many knights do you think you've arrived?"
                        x"If you die anyway, the King will keep finding new people to become knights."
                        e"you lie"
                        x"NO"
                        x"that truth"
                        x"That king was a scum, making a living with the people and acting as if to help when he was happy on one side."
                        x"You die and it finds someone new to replace it and keeps pretending to collect taxes from new people. To come to a knight like you knowing that sent you to die"
                        d"Choose your way"

                        menu:
                            "HONOR":
                                jump bossfight
                            "You way":
                                jump bossdark

                        label bossfight:
                            scene bossroomfight1
                            show invisible
                            with fade
                            e"LIE"
                            e"You LIE"
                            e"I wANNA KILL YOU"

                            scene bossroomfight2
                            show invisible
                            with fade
                            e"..."

                            scene bossroomfight3
                            show invisible
                            with fade
                            d"You died"
                            d"you die with honor"
                            d"you lose the fight"
                            d"The king make grave for you"
                            d"for you and for the knights before you"
                            d"And probably for new knights too."

                            scene bossroomdark1
                            show invisible
                            play music "audio/endcredit.mp3"
                            empty "You died [die]"
                            return

                        label bossdark:
                            scene bossroomdark1
                            show invisible
                            with fade
                            e"You choose dark sight"

                            scene bossroomdark2
                            show invisible
                            with fade
                            e"You go to kill the king"

                            scene bossroomdark3
                            show invisible
                            with fade
                            k"Argh!!!"
                            k"I am sorry"
                            k"don't kill me"
                            k"I have a lot of money, take it."
                            k"I have slaves, take them all. Want to kill people? Go kill the poor people in my city, there are a lot of them, you can kill as many as you want. please spare my life"
                            e"..."
                            e"disgusting"
                            e"you are disgusting"
                            k"ARKK!!!!!!"

                            scene bossroomdark4
                            show invisible
                            with fade
                            e"You deserve to die"
                            e"I will be the king"
                            e"I will make everyone choose their own path."
                            scene bossroomdark1
                            show invisible
                            play music "audio/endcredit.mp3"
                            empty "You died [die]"
                            return

        label walk:
            scene walk1
            show invisible
            with fade
            e "Just walk>"
            scene walk2
            show invisible
            with fade
            e "la la la"
            scene walk3
            show invisible
            with fade
            e "Arrow?"
            scene walk4
            show invisible
            with fade
            e "Hmm"
            scene walk5
            show invisible
            with fade
            e "Arghh!!!"
            scene walk6
            show invisible
            with fade
            play sound "audio/smash.mp3"
            e "Then I took an arrow in the knee"
            e "I died"
            jump died
    jump died
    label bg2:
        scene gun1
        show invisible
        with fade
        e "Wow that so cool"
        e "I want to test this"
        e "1"
        e "2"
        e "3"
        scene gun2
        show invisible
        with fade
        play sound "audio/gun.mp3"
        e "Bang!!!"
        e "argh h"
        d "This gun is shoot from the back."
        jump died

    label bg3:
        scene book1
        show invisible
        with fade
        e "You choose book"
        scene book2
        show invisible
        with fade
        e "open it!"
        scene book3
        show invisible
        with fade
        play sound "audio/booklaser.mp3"
        e "Toom!!!"
        scene book4
        show invisible
        with fade
        e "..."
    jump died
    label bg4:
        e "lazy"
    jump died
label died:
    scene bossroomdark1
    show invisible
    play music "audio/endcredit.mp3"

    $ die += 1

    empty "You died [die]"
    if die == 108:
        return
    jump start
    # This ends the game.

    return
