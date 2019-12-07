"""
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, 
it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""
def lone_sum(a, b, c):
  if(a == b == c):
    a = 0
    b = 0
    c = 0
  if(a == b): 
    a = 0
    b = 0
  if(a == c):
    a = 0
    c = 0
  if(b == c):
    b = 0
    c = 0
  return a + b + c