# Choose your own Adventure Story
# while True:
#     ans = input("seven: ")
#     if ans == "5":
#         print("Correct")
#     else:
#         print("Incorrect")
#     if ans == "5":
#         break
print("CHOOSE YOUR OWN ADVENTURE STORY!")
name = input("Before starting these Adventure, Please enter your Name: ")
print(f"\nHello {name}, my name is Star and I'll instruct and guide you in your Adventures Journey!")
print('''
                 .
             ____/_
  \==      .'__===_|
   \_ _ _ /"---'  \/
   |_|_|_|_\_______\______
   `.==-------------------|_
     `.___________________/

''')
print("It was a hot day and you were very tired of your daily Routine,"
      "\nSo you decided to spend your Weekend on a small cruise alone. "
      "\nYou booked your tickets a day prior. The next day you enjoyed"
      "\na lot on the cruise, it was afternoon and you were resting in"
      "\nyour room, when suddenly a Huge storm appeared from nowhere.")
while True:
    print("\nWhat will you do to survive from this storm?")
    print("1. Wait for someone to Help.")
    print("2. Find out some small ship or vessel and escape from the Storm.")
    strong = input("Type your Answers option number: ")

    if strong == "2":
        print("\nGreat Choice!")
    else:
        print("\nOops!"
              "\nIts so long but no one has arrived to help you, "
              "\nit's a huge storm, try to escape it yourself.")
    if strong == "2":
        break

print("Finally you have escaped from this huge storm.Now you have reached"
          "\nin an Island, it's evening now and you are feeling very hungry,"
          "\nand suddenly you saw something glowing, ohhh! they are glowing"
          "\nmushrooms!")
print('''
  .-"""-.
 /* * * *\\
:_.-:`:-._;
    (_)
 \|/(_)\|/
      ''')
while True:
    print("Will you eat the Glowing Mushroom?")
    print("1. Yes, I'll surely eat it, I can't control my hunger.")
    print("2. I'll prefer to google search it!")
    print("3. No, I won't take any risk and move ahead.")
    precaution = input("Type your Answers option number: ")
    if precaution == "3":
        print("\nGreat Choice!"
              "\nIt's better to not consume anything suspicious, and move"
              "\nahead.\n")
    elif precaution == "2":
        print("\nOops!"
              "\nNo Internet connection available, try other way out!\n")
    else:
        print("\nOops!"
              "\nThat mushroom was poisonous, quickly drink water you'll"
              "\nfeel better and then try other way out!"
              "\n")
    if precaution == "3":
            break

print('''
 ^  ^  ^   ^      ____       ^  ^   ^  ^  ^   ^  ^
/|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\\
/|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\\
/|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\\
    ''')
print("\nOoh, It started raining, you are trying to find some shelter and "
      "\nsuddenly you saw a small Mansion, but you had heard a rumor that"
      "\ntheir is a crazy scientist hiding in the nearby island.")
while True:
    print("\nWhat will you do to survive from the heavy rainfall?\n")
    print("1. I am brave enough, so I'll surely go inside.")
    print("2. No, I won't go, It's fine if I get wet.")
    print("3. I'll prefer to hide under some huge tree.")
    brave = input("Type your Answers option number: ")
    if brave == "1":
        print("\nGreat Choice!"
              "\nYou are pretty brave, Let's continue our journey.")
    elif brave == "3":
        print("\nOops!"
              "\nLightning struck nearby your tree, quickly find out some"
              "\nshelter to hide.")
    else:
        print("\nOops!,"
              "\nNow the rain has turned into thunderstorm, find out some "
              "\nshelter to hide.")
    if brave == "1":
        break
print('''
       __
   _  |@@|
  / \ \--/ __
  ) O|----|  |   __
 / / \ }{ /\ )_ / _\
 )/  /\__/\ \__O (__
|/  (--/\--)    \__/
/   _)(  )(_
   `---''---`
''')
print("Wow! their are some robots standing near the door, it seems that"
      "\nthey are using some code language to enter inside the room it"
      "\ngoes as following:"
      "\nIf the Guard Robot says One, then First Robot says 3"
      "\nIf the Guard Robot says Eleven, then Second Robot says 6")
while True:
    print("\nNow its your Turn, Robot asks you Seven, Whats Your answer?")
    print("1. 4")
    print("2. 5")
    print("3. 7")
    smart = input("Type your Answers option number: ")
    if smart == "2":
        print("\nCorrect Answer!"
              "\nThe logic was too simple 'Seven' Word has 5 letters"
              "\nso the answer is 5")
    else:
        print("\nOops!"
              "\nYour Answer was incorrect, Let's Retry")
    if smart == "2":
        break

print("Ohh, unfortunately the crazy scientist saw you, He has trapped"
      "\nyou in a small cell and wrote a note which includes:"
      "\nHello visitor, I have noticed your bravery and I am giving"
      "\nyou a chance to safely return your home. There are three"
      "\ndoors in front of you,1st door is full of poisonous Snakes,"
      "\nSecond door has a hungry lion which has not ate anything"
      "\nfor 2 months, the third door is a loop, probably endless."
      "\nOnly one of them will lead you to freedom!")
while True:
    print("Which door will you choose")
    print("1. Poisonous Snakes")
    print("2. Hungry Lion")
    print("3. Endless Door")
    logic = input("Type your Answers option number: ")
    if logic == "2":
        print("\nCorrect Choice!")
        print("As the Lion had not ate anything for 2 moths he won't"
              "\nbe alive")
        print(f"\nNow you are at your home. Good Job {name} your are"
              "\npretty brave.I hope will meet soon, with a new Adventure!")
    elif logic == "1":
        print("\nOops!"
              "The snake bite you, lets travel back to time and choose"
              "\nother Door!")
    elif logic == "3":
        print("Oops!"
              "The door brought you back to the Cell!")
    else:
        print("Oops!"
              "Invalid Door")
    if logic == "2":
        break

