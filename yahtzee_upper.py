'''
The game of Yahtzee is played by rolling five 6-sided dice, and scoring the results in a number of ways. 
You are given a Yahtzee dice roll, represented as a sorted list of 5 integers, each of which is between 1 and 6 inclusive. 
Your task is to find the maximum possible score for this roll in the upper section of the Yahtzee score card. Here's what that means.

For the purpose of this challenge, the upper section of Yahtzee gives you six possible ways to score a roll. 
1 times the number of 1's in the roll, 2 times the number of 2's, 3 times the number of 3's, 
and so on up to 6 times the number of 6's. For instance, consider the roll [2, 3, 5, 5, 6]. 
If you scored this as 1's, the score would be 0, since there are no 1's in the roll. If you scored it as 2's, 
the score would be 2, since there's one 2 in the roll. 
Scoring the roll in each of the six ways gives you the six possible scores:

0 2 3 0 10 6

The maximum here is 10 (2x5), so your result should be 10

'''
def yahtzee_score(rolls):
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    six_count = 0
    
    for i in range(len(rolls)):
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
        
    max_value = max(one_count, two_count, three_count, four_count, five_count, six_count)    
    
    return max_value    
    
print(yahtzee_score([2, 3, 5, 5, 6]))
print(yahtzee_score([1, 1, 1, 1, 3]))
print(yahtzee_score([1, 1, 1, 3, 3]))
print(yahtzee_score([1, 2, 3, 4, 5]))
print(yahtzee_score([6, 6, 6, 6, 6]))