"""
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. 

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
"""

def make_bricks(small, big, goal):
  while(goal >= 5) and (big > 0):
    goal = goal - 5
    big = big - 1
  while(goal > 0) and (small > 0):
    goal = goal - 1
    small = small - 1
  
  if (goal == 0):
    return True
  else:
    return False
  
