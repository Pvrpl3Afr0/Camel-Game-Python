#Revisited Camel Game
import random

done = False

miles = 0 #Distance traveled in miles.
tiredness = 0 #The camel's tiredness.
thirst = 0 #Thirst level.
nativemiles = -20 #Distance of natives
fullspeed = random.randrange(9,21)
modspeed = random.randrange(4,13)
natspeed = random.randrange(0,8) #Natives speed
canteen = 7#Three drinks in the canteen.

if miles >= 200:
    done = True
if thirst <= -5:
    print("You ded")
if tiredness <= -10:
    print("you tired")
if nativemiles >= miles:
    print("gottem")
print("You just stole a camel! You have a few options.")
print("A. Drink from your Canteen")
print("B. Ahead moderate speed")
print("C. Ahead full speed.")
print("D. Stop for the night")
print("E. Status Check")
print("Q. Quit")

while not done:
    if miles >= 200:
        print("You made it across the desert!")
        done = True
        exit()
    if thirst <= 5:
        print("You died of thirst!")
    if tiredness <= 10:
        print("You and your camel collapsed!")
        done = True
        exit()
    if nativemiles >= miles:
        print("The natives caught up!")
        done = True
        exit()
    user_choice = input("What would you like to do? ")
    if user_choice == "Q" or  user_choice == "q":
            print("You are now done with the game! Goodbye!")
            done = True
    elif user_choice == "E" or user_choice == "e":
            print("You've traveled", miles,"miles")
            print("You have", canteen, "Drinks in your canteen left and have a thirst value of", thirst)
            print("The natives are", nativemiles, "miles behind.")
            done = False

    elif user_choice == "D" or user_choice == "d":
        print("You rest and gain your energy back. Your camel is happy!")
        tiredness = 0
        nativemiles = nativemiles + natspeed

        #send help
    elif user_choice == "C" or user_choice == "c":
        print("You chose to move on full speed ahead.")
        miles = miles + random.randrange(9,21)
        tiredness = tiredness + fullspeed
        thirst = thirst + 2
        nativemiles = nativemiles + natspeed

    elif user_choice == "B" or user_choice == "b":
        print("You chose to move on at moderate speed.")
        miles = miles + modspeed
        tiredness = tiredness + 1
        thirst = thirst + 1
        nativemiles = nativemiles + natspeed

    elif user_choice == "A" or user_choice == "a":
        print("You chose to take a drink")
        canteen = canteen - 1
        thirst = 0

    else:
        print("You put in a wrong input! Try again.")
        done = False

    if canteen <= 0:
        print("You don't have any drinks left!")
    if thirst <= 5:
        print("You've died of thirst!")
        done = True
    if thirst <= 2:
              print("You're dangerously thirsty!")
if done == True:
    exit()
