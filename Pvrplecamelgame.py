#The Camel game by Pvrpl
import random
print("You just stole a camel! You have a few options.")
print("A. Drink from your Canteen")
print("B. Ahead moderate speed")
print("C. Ahead full speed.")
print("D. Stop for the night")
print("E. Status Check")
print("Q. Quit")


done = False
miles = 0 #Distance traveled in miles.
tiredness = 0 #The camel's tiredness.
thirst = 0 #Thirst level.
nativemiles = -20 #Distance of natives

canteen = 3#Three drinks in the canteen.

def game():
    done = False
    miles = 0 #Distance traveled in miles.
    tiredness = 0 #The camel's tiredness.
    thirst = 0 #Thirst level.
    nativemiles = -20 #Distance of natives
    canteen = 3

    user_choice = input("What would you like to do? ")
    if miles >= 200:
        done = True
    while not done:
        if user_choice == "Q" or  user_choice == "q":
                print("You are now done with the game! Goodbye!")
                done = True
        elif user_choice == "E" or user_choice == "e":
                print("You've traveled", miles,"miles")
                print("You have", canteen, "drinks in your canteen left and have a thirst value of", thirst)
                print("The natives are", nativemiles, "miles behind.")
                done = False
        elif user_choice == "D" or user_choice == "d":
            print("You rest and gain your energy back. Your camel is happy!")
            tiredness = 0
            nativemiles = nativemiles + random.randrange(0,8)
            done = False
        elif user_choice == "C" or user_choice == "c":
            print("You chose to move on full speed ahead.")
            miles = miles + random.randrange(9,21)
            tiredness = tiredness + random.randrange(0,4)
            thirst = thirst + 2
            nativemiles = nativemiles + random.randrange(7,14)
        elif user_choice == "B" or user_choice == "b":
            print("You chose to move on at moderate speed.")
            miles = miles + random.randrange(4,13)
            tiredness = tiredness + 1
            thirst = thirst + 1
            nativemiles = nativemiles + random.randrange(7,14)
        elif user_choice == "A" or user_choice == "a":
            print("You chose to take a drink")
            canteen = canteen - 1
            thirst = 0
            if canteen <= 0:
                print("You don't have any drinks left!")
        else:
            print("You input an incorrect option! Try again!")
            return
        break
while not done:
        game()
        if miles >= 200:
            done = True

        else:
            game()
            break

