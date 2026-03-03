#Importing random
import random

print("Hi Sinelya")

#Initialising variables
rows = 16
money = 500
bet = 100

# 16 multipliers 
slots = [10, 5, 3, 2, 1, 0.5, 0.3,0,0,0.3, 0.5, 1, 2, 3, 5, 10]

while True:

    print("You have $",money)
    choice = input("Drop a ball for $100? (yes/no): ")

    if choice == "no":
        print('Smart choice')
        break

#If the money is over
    if money < bet:
        print("You're broke and have an addiction. Hit up the gambling helpline at 0800 654 655 :D")
        break

    money = money - bet
    position = 0

    for r in range(rows):

        #Spacing for the pyramid
        print(" " * (rows - r), end="")
        
        for i in range(r + 1):
            if i == position:
                print("✪ ", end="")
            else:
                print("* ", end="")
        print()

        #Move left or right
        move = random.choice([0, 1])
        position = position + move

        if position > r:
            position = r

    multiplier = slots[position]

#Printing the winning and losses
    print("Landed in slot", position)
    print("Multiplier:", multiplier)

    winnings = bet * multiplier
    money = money + winnings

    print("Amount after multiplication:", winnings)
    print("Money now:", money)

print("Game Over")
print("Final money:", money)
