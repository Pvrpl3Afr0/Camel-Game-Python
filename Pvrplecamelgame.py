#The Camel game by Pvrpl
print("You just stole a camel! You have a few options.")
print("A. Drink from your Canteen")
print("B. Ahead moderate speed")
print("C. Ahead full speed.")
print("D. Stop for the night")
print("E. Status Check")
print("Q. Quit")
user_choice = input("What would you like to do? ")

done = False
miles = 0 #Distance traveled in miles.
tiredness = 0 #The camel's tiredness.
thirst = 0 #Thirst level.
nativemiles = -20 #Distance of natives

canteen = 3#Three drinks in the canteen.
def game():
    if user_choice == "Q" or  user_choice == "q":
            print("You are now done with the game! Goodbye!")
            done = True
    elif user_choice == "E" or "e":
            print("You've traveled", miles,"miles")
            print("You have", canteen, "drinks in your canteen left and have a thirst value of", thirst)
            print("The natives are", nativemiles, "miles behind.")
    elif user_choice == "D" or "d":
        print("You rest and gain your energy back. Your camel is happy!")
        tiredness = 0
        nativemiles = nativemiles + random.randrange(0,8)
    elif user_choice == "C" or "c":
        print("You chose to move on full speed ahead.")
        miles = miles + random.randrange(9,21)
        tiredness = tiredness + random.randrange(0,4)
        thirst = thirst + 2
        nativemiles = nativemiles + random.randrange(7,14)
    elif user_choice == "B" or "b":
        print("You chose to move on at moderate speed.")
        miles = miles + random.randrange(4,13)
        tiredness = tiredness + 1
        thirst = thirst + 1
        nativemiles = nativemiles + random.randrange(7,14)
    elif user_choice == "A" or "a":
        print("You chose to take a drink")
        canteen = canteen - 1
        thirst = 0
        if canteen <= 0:
            print("You don't have any drinks left!")

while done is False:
        game()
        break
