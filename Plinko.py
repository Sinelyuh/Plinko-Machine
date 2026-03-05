#Importing random
import random

#Initialising variables
rows = int(input('Enter the amount of rows (8/12/16):'))
while rows!=8 and rows!=12 and rows!=16:
    rows = int(input('Enter the amount of rows (8/12/16):'))
money = 500
bet = int(input('How much do you want each bet to be (no more than 500):'))
while bet>500:
    bet = int(input('How much do you want each bet to be (no more than 500):'))
    

# 8/12/16 multipliers
slots=[]
if rows==8:
    slots=[13,3,1.3,0.7,0.4,0.7,1.3,3,13]
elif rows==12:
    slots=[33,11,4,2,1.1,0.6,0.3,0.6,1.1,2,4,11,33]
else:
    slots = [110,41,10,5,3,1.5,1,0.5,0.3,0.5,1,1.5,3,5,10,41,110]

#Starting the game
while True:

    print("You have $",money)
    choice = input('Drop a ball? (yes/no):')

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

            #To get the indexes
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
