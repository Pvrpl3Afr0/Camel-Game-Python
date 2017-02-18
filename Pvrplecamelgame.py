#The Camel game by Pvrpl

done = False

while done is False:
        print("A. Drink from your Canteen")
        print("B. Ahead moderate speed")
        print("C. Ahead full speed.")
        print("D. Stop for the night")
        print("E. Status Check")
        print("Q. Quit")
user_choice.upper() = input("What would you like to do? ")

if user_choice == "Q":
    print("You are now done with the game! Goodbye!")
    done = True
