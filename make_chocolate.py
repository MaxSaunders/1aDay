"""
We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars 
before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""

def make_chocolate(small, big, goal):
  count = 0
  while(goal >= 5) and (big > 0):
    goal = goal - 5
    big = big - 1
    
  while(goal > 0) and (small > 0):
    goal = goal - 1
    small = small - 1
    count += 1
  if(goal > 0):
    return -1
  
  return count
