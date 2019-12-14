'''
The game of Yahtzee is played by rolling five 6-sided dice, and scoring the results in a number of ways. 
You are given a Yahtzee dice roll, represented as a sorted list of 5 integers, each of which is between 1 and 6 inclusive. 
Your task is to find the maximum possible score for this roll in the game of yahtzee"


'''
def yahtzee_check(rolls):
    return len(set(rolls)) == 1
    
def check_small(rolls):             #checks for small straight starting from first integer to second to last
    i = 1
    count = 1
    while i < (len(rolls) - 1):
        if(rolls[i] != rolls[i - 1] + 1):
            return False
        i += 1
    return True

def second_small_check(rolls):      #checks for small straight starting from 2nd integer to last
    i = 2
    count = 1
    while i < (len(rolls)):
        if(rolls[i] != rolls[i - 1] + 1):
            return False
        i += 1
    return True
    
    
def check_big(rolls):
    i = 1
    count = 1
    while i < (len(rolls)):
        if(rolls[i] != (rolls[i - 1]) + 1): #this checks that each item in the list is equal
            return False                    #to 1+ the integer that came before
        i += 1
    return True
    
def full_check(r):              #check if rolls contain a full house (3 of a kind and a pair)
    i = 1
    if(r[0] == r[1]):           #checks if the first 2 integers are equal since the list is sorted
                                #the first 2 will be equal if it has a full house
        if(r[0] == r[2] and r[3] == r[4]):  #checks if the first 2 are equal to the 3rd and the 4th and 5th are equal
            return True
        if(r[2] == r[3] and r[2] == r[4]):  #else checks if the 3rd, 4th, and 5th are equal
            return True
    return False                            #if any are false it returns false
    
def yahtzee_score(rolls):
    rolls.sort()
    
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    six_count = 0
    three_kind = 0
    four_kind = 0   
    full_house = 0  #a pair and a 3 of a kind
    small = 0       #small straight (4 in a row)
    big = 0         #big straight (5 in a row)
    yahztee = 0     #5 of a kind
    chance = 0      #the sum of all dice with no patterns
    
    if (yahtzee_check(rolls) == True):    #checks for yahtzee
        return "Yahtzee!: 50 Points!!"
    
    if(full_check(rolls) == True):          #Full House check
        full_house = 25
    
    #checks for small straight
    if(check_big(rolls) == True):
        big = 40
    elif(check_small(rolls) == True):
        small = 30
    elif(second_small_check(rolls) == True):
        small = 30
       
       
    #checks for big straight
    
        
    
    for i in range(len(rolls)):     #checks for the "upper" scores
        if rolls[i] == 1:
            one_count += 1
        if rolls[i] == 2:
            two_count += 2
        if rolls[i] == 3:
            three_count += 3
        if rolls[i] == 4:
            four_count += 4
        if rolls[i] == 5:
            five_count += 5
        if rolls[i] == 6:
            six_count += 6
            
    #check for 3 of a kind
    if(six_count == 18):
        three_kind = sum(rolls)
    if(five_count == 15):
        three_kind = sum(rolls)
    if(four_count == 12):
        three_kind = sum(rolls)
    if(three_count == 9):
        three_kind = sum(rolls)
    if(two_count == 6):
        three_kind = sum(rolls)
    if(one_count == 3):
        three_kind = sum(rolls)
     
    #checks for 4 of a kind   
    if(six_count == 24):
        four_kind = sum(rolls)
    if(five_count == 20):
        four_kind = sum(rolls)
    if(four_count == 16):
        four_kind = sum(rolls)
    if(three_count == 12):
        four_kind = sum(rolls)
    if(two_count == 8):
        four_kind = sum(rolls)
    if(one_count == 4):
        four_kind = sum(rolls)
    
    chance = sum(rolls)
    
        
    max_value = max(yahztee, full_house, chance, four_kind, three_kind, small, big, one_count, two_count, three_count, four_count, five_count, six_count)    
    
    #determine which variable has the highest value and prints the variable name
    out = "The best choice is \n"
    if(max_value == four_kind):
        out += "Four of a kind: "
    elif(max_value == three_kind):
        out += "Three of a kind: "
    elif(max_value == big):
        out += "Big Straight: "
    elif(max_value == small):
        out += "Small Straight: "
    elif(max_value == six_count):
        out += "Sixes: "
    elif(max_value == five_count):
        out += "Fives: "
    elif(max_value == four_count):
        out += "Fours: "
    elif(max_value == full_house):
        out += "Full House: "
    
    
    out += str(max_value)
    out += " Points\n"
    return out    
    
#print(yahtzee_score([2, 3, 4, 5, 6]))
#print(yahtzee_score([1, 1, 1, 1, 3]))
#print(yahtzee_score([1, 1, 1, 3, 3]))
#print(yahtzee_score([2, 2, 3, 4, 5]))
#print(yahtzee_score([6, 6, 6, 6, 6]))
#print(yahtzee_score([4, 6, 3, 6, 6]))
print(yahtzee_score([4, 1, 4, 1, 1]))