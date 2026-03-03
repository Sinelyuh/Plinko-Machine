#Importing random
import random

print("Hi Sinelya")

#Initialising variables
rows = 16
money = 500
bet = 100

# 16 multipliers 
slots = [10, 5, 3, 2, 1, 0.5, 0.3,0,0,0.3, 0.5, 1, 2, 3, 5, 10]


#Starting the game
while True:

    print("You have $",money)
    choice = input("Drop a ball for $100? (yes/no): ")

    #If the user says no the loop breaks
    if choice == "no":
        print('Smart choice')
        break

#If the money is over
    if money < bet:
        print("You're broke and have an addiction. Hit up the gambling helpline at 0800 654 655 :D")
        break

    #Removing the bet from the amount they had
    money = money - bet
    position = 0

    #To loop through the rows
    for row in range(rows):

        #Spacing for the pyramid
        print(" " * (rows - row), end="")

            #To get the indextes
        for i in range(row + 1):
            if i == position:
                print("✪ ", end="")
            else:
                print("* ", end="")
        print()

        #Move left or right
        move = random.choice([0, 1])
        position = position + move

        #To check the end position
        if position > row:
            position = row

    multiplier = slots[position]

#Printing the winning and losses
    print("Landed in slot", position)
    print("Multiplier:", multiplier)

    #Multiplying the winnings
    winnings = bet * multiplier
    money = money + winnings

    print("Amount after multiplication:", winnings)
    print("Money now:", money)

print("Game Over")
print("Final money:", money)
