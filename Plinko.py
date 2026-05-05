#Importing random
import random

#Initialising the variables
money=500

def getting_bet(money):
    while True:
        try:
            bet = int(input('Enter your bet (max 500): '))
            
            if bet > 500 or bet > money:
                print("Bet is too high!")
            elif bet <= 0:
                print("Bet must be greater than 0.")
            else:
                return bet  
        except:
            print("Please enter a valid number.")

def getting_row():
    ''' Getting the row number from the user'''
    while True:
        try:
            row = int(input('Enter the amount of rows (8/12/16):'))
            if row != 8 and row != 12 and row!=16:
                print("Enter 8,12 or 16 please.")
            else:
                break       # Only break once int entered
        except:
            print("Enter a real number.")
    return row    
        


#Function for the 8/12/16 multipliers
def slots(rows):
    '''Getting the difficulty through the number of rows'''
    slots=[]

    #Checking the users preferred row
    if rows==8:
        slots=[13,3,1.3,0.7,0.4,0.7,1.3,3,13]
        return slots
    elif rows==12:
        slots=[33,11,4,2,1.1,0.6,0.3,0.6,1.1,2,4,11,33]
        return slots
    else:
        if rows==16:
            slots= [110,41,10,5,3,1.5,1,0.5,0.3,0.5,1,1.5,3,5,10,41,110]
            return slots
        
#Third function
def loop_through_rows(row,position,active_slots):
    '''Loop through each row an display as the ball falls down'''

    # Looping through the size of the row
    for row_one in range(row):
        
            #Spacing for the pyramid
            print(" " *(row-row_one),end="")

            #To get the indexes of the ??
            for i in range(row_one+1):
                if i==position:
                    print("✪ ",end="")
                else:
                    print("* ",end="")
            print()

            #Move left or right
            move=random.choice([0,1])
            position=position+move

            #To check the end position
            if position>row_one:
                position=row_one

            multiplier=active_slots[position]
    return multiplier,position

#Main program
if __name__=='__main__':
    
    #Getting the rows
    user_row=getting_row()
    
    #Getting bet
    user_bet=getting_bet(money)
    
    #Getting the multipliers
    active_slots =slots(user_row)

        #Starting the game
    while True:

        print("You have $",money)
        choice=input('Drop a ball? (yes/no):')

        #If the user says no the loop breaks
        if choice=="no":
            print('Smart choice')
            break

    #If the money is over
        if money<user_bet:
            print("You're broke and have an addiction. Hit up the gambling helpline at 0800 654 655 :D")
            break

        #Removing the bet from the amount they had
        money=money-user_bet
        position=0

        #To loop through the rows (function)
        multiplier, position = loop_through_rows(user_row, position, active_slots)
        
    #Printing the winning and losses
        print("Landed in slot",position)
        print("Multiplier:",multiplier)

        #Multiplying the winnings
        winnings=user_bet*multiplier
        money=money+winnings

        print("Amount after multiplication:",winnings)
        print("Money now:",money)

    print("Game Over")
    print("Final money:",money)
