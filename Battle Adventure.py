age = input("Welcome to Battle Adventure.\n"
            "Whats your age? - ")
name = input("Whats your name? - ")
print(f"Welcome {name}, this is the journey of a lifetime!\nEspecially at the ripe old age of {age}.\n")
print(f"Alright {name}, i hope you are ready because here we go!\n")
q1 = input("You wake up in an open field, nothing around for miles\n"
           "except for a small wooden cabin to your left.\n"
           "Which way do you go? right or left - ")

if q1 == str("left"):
    print("As you approach the cabin, a lone wolf comes out to eat you,\n"
          "Game Over!")
    exit()

elif q1 == str("right"):
    print("\nThe cabin gives you overwhelming dread\n"
          "so you walk away and head right.\n")

    q2 = input("As you walk, you see a mountain looming in the distance.\n"
               "The closer you get the clearer the mountain comes into view.\n"
               "You spot an opening in the mountain, its a cave, what do you do?\n"
               "enter or avoid? - ")

    if q2 == str("avoid"):
        print("The cave brings you fear so you avoid it at all cost.\n"
              "What you didn't realize tho was that something has been hunting you this entire journey.\n"
              "Before you can react, you were stabbed in the back and dragged off to an unknown fate.\n"
              "Game Over!")
        exit()

    elif q2 == str("enter"):
        print("\nApproaching the cave you spot something shining just inside the mouth of the cave.")

        q3 = input("\nPeering closer to this shining object, you see its a sword.\n"
                   "A closer look at this sword you see that is covered in rust,\n"
                   "the edge looks dull, and it looks completely worthless.\n"
                   "What do you do?\n"
                   "take or leave. - ")

        if q3 == str("leave"):
            print(f"\n{name} decided to leave that dumb old sword.\n"
                  f"What he didn't realize was that the 'dumb old rusted sword' was going to come in handy\n"
                  "very soon.\n\n"
                  f"{name} walks away from the cave empty handed and as we passes by a rock, a bloodthirsty \n"
                  f"Monster jumps ontop of him and bites into his neck, killing {name} instantly.\n"
                  f"Game Over!")
            exit()


        elif q3 == str("take"):
            print(f"{name} reaches in and grabs the old sword with both hands.\n"
                  f"With a powerful pull {name} removes the sword from the cave and keeps it close.\n")

            q4 = input(f"After grabbing the sword, you decide to make camp.\n"
                  f"{name} lights up a fire and gets ready to get to sleep.\n"
                  f"As {name} starts to drift off to sleep {name} hears a noise.\n\n"
                  f"{name} can sense a evil presence near by, {name} lifts up the sword and...\n"
                  f"Do you \n"
                  f"a - lift the sword and throw it at the noise.\n"
                  f"b - charge into the darkness ready for anything\n")

            if q4 == "a":
                print("The sword fly's through the air hitting absolutely nothing.\n"
                      "You are now completely defenseless as the monster that's been following you\n"
                      "guts you like a fish\n"
                      "Game Over!")
                exit()

            elif q4 == "b":
                print("As you bravely charge into the forest completely blind due to no light,\n"
                      "you somehow manage to pierce the monster that's been following you since you woke up.\n"
                      "As the blood coats your newly acquired blade, the mystical mysterious sword starts to glow.\n"
                      "With the sword stuck inside the monsters gut, the blade glows brighter and brighter.\n"
                      "As the monster screams in pain from the stab, the blade glows so bright, it detonates from\n"
                      "inside the monsters wound cavity splitting the monster in half.\n"
                      "With the monster destroyed and you safe, your journey comes to an end.")
            else:
                print("invalid answer.")
            print(f"Congratulations adventurer, you've defeated the evil monster and saved the mystical\n"
                  f"sword from the cave. \n\nYou Win {name} The Monster Slayer!!")

        else:
            print("invalid answer.")



    else:
        print("invalid answer.")

else:
    print ("invalid answer.")
