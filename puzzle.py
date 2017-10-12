"""possible endings: user gets abducted, alien goes back to planet in defeat (outfitted with Earthly swag attire),
alien lives on Earth and co-exists with humans peacefully,
user saves Earth"""

from sys import exit
import random


class color:
   PURPLE = '\033[95m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def candy():
   print("The mothership just landed in East Village on Halloween evening.")

#print(f"We have been observing your planet for a long time.")
   print("\nWe are now taking control of the planet as we've seen the disintegration of the political, social and environmental fabric by the hands of the human race.")

   print(color.BOLD + "\nYou have three options: take the" + color.END + color.BOLD + " Gummi Bears, " + color.END + "take the" + color.BOLD + " Jolly Ranchers " + color.END + "or if you dare to take, the" + color.BOLD + " Third Option" + color.END + ".")


   selection = input("\nWhich do you choose:" + color.YELLOW + " Gummi Bears, " + color.END + color.YELLOW + " Jolly Ranchers, " + color.END + "or the" + color.YELLOW + " Third Option" + color.END + "? ")

   if selection == "Gummi Bears":
       print("\nThe" + color.BOLD + " Gummi bears " + color.END + "will transform your mind, body and soul.")
       print("\nHowever, it may mean the memories of your old life will be wiped out.")
       print("\nLeaving you with a human shell but without the emotional feelings that humans are known to prioritize.")
       choice = input(color.BOLD + "Do you accept:" + color.END + color.YELLOW + " yes" + color.END + " or " + color.YELLOW + "no" + color.END + "? ")

   elif selection == "Jolly Ranchers":
       print("\nThe" + color.BOLD + " Jolly Ranchers " + color.END + "will transmit the knowledge as it existed from the start of time into your brain.")
       print("\nThere will be no need for spoken word or language. The human race will have no conflict")
       print("\nThe future is in your hands.")
       print("\nPick a number between 1-100 to determine whether you will advance.")

       number = int(input(" Enter a number:  "))

       if (number>=0 and number<=25):
           print(f"You shall pass.")
       if (number >=26 and number <= 50):
           print(f"You shall pass.")
       if (number >=51 and number <=75):
           print(f"You shall not pass.")
       if (number >=76 and number <=100):
           print(f"You shall not pass.")

       elif selection == "Third Option":
           print("You are a risk taker, but the fate of the" + color.BLUE + " Earth " + color.END + "depends on your selfless act.")

   else:
       probed()


def probed():
       print("Excellent choice! You will be going to the enchanted Forest.")


def alive(forest):

   print("The potion of Courage will help protect you against the demons that will seek to harm you.")
   selection = input(" >")

candy()




def outside():
    print("Here you see the" + color.GREEN + " aliens " + color.END + "as they land in Times Square.")


def kill_alien():
    print("You just shot the" + color.GREEN + " alien " + color.END + "out of fear.")
    print("You just started an intergallactic war and you are outgunned!")
    dead("You are trigger happy, but dead --- ")


def outside2():
    print("You run out the door to see the" + color.GREEN + " aliens " + color.END + "walking out the mothership.")
    print(color.RED + "\nWhat do you do?" + color.END)
    print(color.YELLOW + " 1. " + color.END + "Go to the nearest bodega and grab some flowers to \nwelcome" + color.GREEN + " aliens " + color.END + "to" + color.BLUE + " Earth " + color.END + ".")
    print(color.YELLOW + " 2. " + color.END + "You can't believe this is actually happening and \nthink it's a major marketing campaign.")
    print(color.YELLOW + " 3. " + color.END + "You grip your handgun and prepare to greet the \ngreys with lead!")
    print(color.YELLOW + " 4. " + color.END + "You pull your handgun and shoot at the" + color.GREEN + " aliens!" + color.END)
    encounter = input(" ")

    if encounter == "1":
        print("Aliens have no use for bodega flowers!")
        print("The" + color.GREEN + " aliens " + color.END  + "see the gesture as you offering yourself to be probed and take you aboard the mothership!")
        Spacecraft_Op_Room()

    if encounter == "2":
        print("You are distracted and should look to do something else.")
        encounter_continued()

    if encounter == "3":
        print("You have a choice to" + color.YELLOW + " shoot  " + color.END + "or" + color.YELLOW + " not shoot " + color.END + ".")
        action = input(color.YELLOW + " Shoot  " + color.END + "or" + color.YELLOW + " not shoot " + color.END + "?")

    if encounter == "4":
        print("Bang-bang!!!")
        kill_alien()


def encounter_continued():
    print(color.RED + " What do you do? " + color.END)
    print(color.YELLOW + " \n1. " + color.END + "Go to the nearest bodega and grab some flowers to welcome" + color.GREEN + " aliens " + color.END + "to" + color.BLUE + " Earth " + color.END + ".")
    print(color.YELLOW + " 2. " + color.END + "You can't believe this is actually happening and think it's a major marketing campaign.")
    print(color.YELLOW + " 3. " + color.END + "You grip your handgun and prepare to greet the greys with lead!")
    print(color.YELLOW + " 4. " + color.END + "You pull your handgun and shoot at the" + color.GREEN + " aliens!" + color.END)

    encounter = input("Enter a number from" + color.YELLOW + "1-4" + color.END + ": ")

    if encounter == "1":
        print(color.BOLD + "\nAliens have no use for bodega flowers!" + color.END)
        print("The" + color.GREEN + " aliens " + color.END + "see the gesture as you offering yourself to be probed and take you aboard the mothership!")
        Spacecraft_Op_Room()

    if encounter == "2":
        print(olor.BOLD + "\nYou are distracted and should look to do something else." + color.END)
        encounter_continued()

    if encounter == "3":
        print(color.BOLD + "\nYou get scared and look for a place to hide." + color.END)
        print(color.YELLOW + " 1. " + color.END + "You run to hide")
        print(color.YELLOW + " 2. " + color.END + "You hide behind a car.")
        print(color.YELLOW + " 3. " + color.END + "You shoot out of fear!")
        action = input()

    if encounter == "4":
        print("\nBang-bang!!!")
        kill_alien()





def room_with_a_view():
    print("You enter the next room and there is a large window.")
    print("You look out the window and see the mothership landing in Times Square.")
    print("You make your way back outside")
    outside2()


def dead(why):
    print(why, "Good job!")
    exit(0)


def Spacecraft_Op_Room():
    print("\nYou now find yourself strapped-in on a table being probed.")
    print("You communicating with the" + color.GREEN + " aliens " + color.END + "around you through telepathic means.")
    print("You get the attention of the aliens and you tell them to:")
    print("\n \t" + color.YELLOW + " 1. " + color.END + "Let you go!")
    print("\t" + color.YELLOW + " 2." +color.END + " Continue probing you, you actually enjoy it.")

    set_me_free = input("\nEnter a number" + color.YELLOW + " 1" + color.END +  " or " + color.YELLOW + "2" + color.END + "? : ")

    if set_me_free == "1":
        print(color.BOLD + "The aliens comply and wish you well" + color.END)
    elif set_me_free == "2":
        print("\nThe" + color.GREEN + " aliens " + color.END + "continue the probing and insert a triangular chip under your clavicle.")


def Cat_Is_Purrfect():
    print("\nYou give the" + color.GREEN + " alien " + color.END + "a pet cat as a symbol of friendship.")
    print("Who knew that" + color.GREEN + " aliens " + color.END + "liked cute little fur balls?")


def start():
    print("\nYou are in a dark room.")
    print("There is a door to open on your" + color.YELLOW + " right" + color.END + " and " + color.YELLOW + "left." + color.END)
    print(color.RED + "\nWhich one do you take?" + color.END)

    choice = input("> ")

    if choice == "left":
        room_with_a_view()
    elif choice == "right":
        outside()
    else:
        dead("You stumble around the room until you starve.")

start()


def alien_not_shot():
    shot_at = (random.randint(1,3))
    if shot_at == 1:
        print("You miss and the" + color.GREEN + " alien " + color.END + "shoots back")
        #shoot_back = (random.randint(1,3))
    else:
        print("\nYou shoot" + color.GREEN + " alien " + color.END + "dead")

    if shot_at == 2:
        shoot_back = (random.randint(1,3))
        if shoot_back == "1":
            print(color.GREEN + " Alien " + color.END + "is a great shot and critically wounds you!")
        else:
            (color.GREEN + " Alien " + color.END + " misses and you get to live, for now.")
    else:
        print("\nYou dodge the laser and are able to escape.")
        escape_alien()


def alien_not_shoot():
    print("By not shooting you have proven to the" + color.GREEN + " aliens " + color.END + "that all humans aren't bad.")
    Cat_Is_Purrfect()


def escape_alien():
    print(color.BOLD + "You make it to nearby building." + color.END + color.RED + " What do you do? " + color.END)
    print(color.YELLOW + "\n1 " + color.END + "will take you into building" + color.YELLOW + " \n2 " + color.END + "will allow you to hide behind a pillar.")
    escape = input("Enter a number" + color.YELLOW + " 1 " + color.END + "or" + color.YELLOW + " 2 " + color.END + " here: ")

    if escape == "1":
        print("\nThe building has a security officer who is telling you to leave!")
        print("You go back outside and are confronted by the" + color.GREEN + " alien " + color.END + "who \nspeaks using unintellegible words.")
    elif escape == "2":
        print("You hide like a quivering coward behind a pillar.")
        print("The" + color.GREEN + " alien " + color.END + "easily finds you and speaks to you using unintellegible words. ")


def ending():
    print("\nThe Sun is now rising in the East")
    print("You have a choice, the fate of humanity is in your hands,\n" + color.RED + "What will you do?" + color.END)
    print("-Offer yourself to be" + color.YELLOW + " abducted" + color.END + "?")
    print("-Offer your cute cat to" + color.YELLOW + " appease " + color.END + "the enamored alien?")
    print("-You decide to" + color.YELLOW + " shoot " + color.END + "or" + color.YELLOW + " not shoot " + color.END + "alien!")

    choice = input(color.RED + "Your decision here:> " + color.END)

    if choice == "abducted":
        Spacecraft_Op_Room() # User gets abducted.
    elif choice == "appease":
        Cat_Is_Purrfect() #Alien lives on Earth & co-exists with human peacefully.
    elif choice == "shoot":
        shot_at = (random.randint(1,101))
        if shot_at %2 == 0:
            kill_alien()

        else:
            dead("You have been zapped by" + color.GREEN + " alien " + color.END)

    elif choice == "not shoot":
        alien_not_shoot()

ending()
