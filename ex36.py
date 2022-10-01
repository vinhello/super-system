# import the exit function from the sys module
from sys import exit
from sys import argv

# function if the fly power is selected
def fly_room():
    print("You have chosen the power to fly.")
    print("You now travel to Arachne's lair. Prepare for battle!")
    print("You use your power and fly up into the air.")
    print("How many molotov cocktails do you drop on Arachne?")

    # assigns the players decision with the variable choice
    choice = input("> ")

    # tries to run the code, if an error appears then throws a response with except
    try:
        # uses int function to turn the input which is a string by default into an integer
        how_many = int(choice)

        # defines thresholds and actions for number of molotovs dropped on arachne
        # if less than or equal to 5
        if how_many <= 5:
            dead("That is not enough.")

        # if great than 5 and less than or equal to 10, weaken arachne and gives player another chance to take an action
        elif how_many > 5 and how_many <= 10:
            print("You have weaken Arachne! But she is preparing to strike. Do you dodge or attack?")

            # ask for player input on what action to take
            decision = input("> ")

            if decision == "dodge":
                dead("You were not fast enough.")
            # win
            elif decision == "attack":
                print("Arachne shrieks in agony! Her eight legs curl up and she dies. You win!!")
            else:
                dead("Your actions don't make sense. Arachne swipes into the air and knocks you to the ground.")

        # if greater than 10
        # win
        elif how_many > 10:
            print("You incinerated Arachne. You win!!")
            exit(0)

    # if an error is thrown then kill code
    except ValueError:
        dead("Your actions don't make sense. Arachne swipes into the air and knocks you to the ground.")

# define the function if player chooses invisibility
def invisibility_room():
    print("You have chosen the power of invisibility.")
    print("You now travel to Arachne's lair. Prepare for battle!")
    print("You get close to Arachne and hide behind a rock. What do you do next?")

    # defines var x providing options for the player
    x = ["attack", "invisible", "yell", "run"]

    # prints options for the player
    print(x)

    # defines var choice and assigns the players input to that var
    choice = input("> ")

    # tries to run the code, if an error appears then throws a response with except
    try:

        # if player chooses attack then dead
        if choice == "attack":
            print("Arachne immediately sees you.")
            dead("It's pincers immediates wrap around your body.")

        # if player chooses invisible then provide more options
        elif choice == "invisible":
            print("You turn invisible and blend into your surroundings.")
            print("You stealthly walk to Arachne until you are face to face.")

            # define var i with a numerical value of 0
            i = 0

            # create a while loop that keeps looping so long as var i is less than 3
            while i < 3:

                print("You pull out your dagger and can stab Arachne 3 times. You need to stab the targets in the right order!")

                # the player needs to stab arachne in the correct order but they only get 3 trys
                # prints the options for the player to choose from
                targets = ["fangs", "eyes", "body"]
                print(targets)

                # ask for the players first input
                print("What do you stab first?")
                t1 = input("> ")

                # ask for the players second input
                print("What do you stab second?")
                t2 = input("> ")

                # ask for the players third input
                print("What do you stab last?")
                t3 = input("> ")

                # define var order and creates a list out of the players inputs
                order = [t1, t2, t3]

                # if player chooses the correct order then player wins
                if order == ["eyes", "fangs", "body"]:
                    print("Arachne hisses in agony and collapses. You win!")
                    exit(0)
                # if player does not pick the right order in 3 trys, they die
                elif i >= 3:
                    print("Arachne has had enough. She retracts and expells acid from her mouth.")
                    dead("You melt to the ground.")
                # this incrementally adds a value of 1 to var i, if the player takes more than 3 tires, they lose
                else:
                    print("Arachne winces in pain but it is not enough!")
                    i = i + 1

            # once the players 3 guesses are spent, they lose
            print("Arachne grows tired of you. She retracts and expells acid from her mouth.")
            dead("You melt to the ground.")

        # if player chooses yell then they die
        elif choice == "yell":
            print("You fool! Arachne immediately turns in your direction.")
            dead("Arachne jumps into the air and crushes your body.")
        # if the player chooses run then they die
        elif choice == "run":
            print("Arachne sees you fleeing and shoots her web at you. You get knocked to the ground.")
            dead("Everything is dark. You feel your body rolling in circles as more web tightens. Sharp fangs enter your back.")
        # if the user inputs aren't from the above options then restart the function
        else:
            print("That doesn't make sense. Try again.")
            invisibility_room()

    # if an error is thrown when the code is run then run the dead function
    except ValueError:
        dead("Your actions don't make sense. Arachne tramples you.")

# define strength_room function
def strength_room():
    print("You have chosen the power of strength.")
    print("You now travel to Arachne's lair. Prepare for battle!")
    print("You get close to Arachne and hide behind a rock. What do you do next?")

    # define var x with a list of the players options
    x = ["Enter \"1\" to spin-throw Arachne down a cliff", "Enter \"2\" to jump-slam into Arachne", "Enter \"3\" to perform a backbreaker on Arachne"]

    # print the options for the player
    print(x)

    # define an infinite while loop until the player chooses the correct options
    while True:

        # define var choice and assign players input to that var
        choice = input("> ")

        # if player chooses 1 then they win
        if choice == "1":
            print("Arachne goes flying off the cliff into the darkness. Only time will tell if that was truly her end...")
            exit(0)

        # else if player chooses 2 then player dies
        elif choice == "2":
            print("You slam into Arachne with your newfound strength. But her blood is made of acid!")
            dead("You quickly realize your mistake as you melt.")

        # else if player chooses 3 then the player wins
        elif choice == "3":
            print("You launch Arachne into the air. Holding on to her arms you bring her thorax down on your knee. She crumples into a dark mass. You win!")
            exit(0)

        # else if player does not choose any of those answers then the player will be prompted to choose again
        else:
            print("That makes no sense! Choose again. But wisely...")
            # repeats the options listed in var x
            print(x)

# define dead function to exit program
def dead(why):
    print(why, "You died.")
    exit(0)

# this function starts the game
def start():
    print("Mooks...")
    print("Mooks......")
    print("Wake up, Mooks. The town of Olnyou needs your help.")
    print("The vile spider queen, Arachne has created her lair in the nearby forest and is preying on the townsfolk!")
    print("We need you to vanquish her so the people of Olnyou can live in peace.")
    print("I can help. I am the power gremlin B.D. Sam. By granting you a power we stand a chance against Arachne.")
    print("You can choose between these powers: flight, invisibility, or strength.")
    print("Which do you choose?")

    # while loop that will infinitely prompt the player until one of 3 powers is selected
    while True:
        choice = input("> ")

        # takes player to fly_room function
        if choice == "flight":
            fly_room()
        # takes player to invisibility_room function
        elif choice == "invisibility":
            invisibility_room()
        # takes player to strength_room function
        elif choice == "strength":
            strength_room()
        # other values that are not one of the ones above will cause the loop to repeat itself
        else:
            print("That is not a choice. Try again.")

# starts the program
start()
