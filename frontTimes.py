"""
Given a string and a non-negative int n, 
we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. 
Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""
def front_times(str, n):
  front = ""
  b = 0
  while(b < len(str)):  #stops the loop when we hit the last char
    if(b >= 3):     #breaks if the loop tries to go past 3rd char
      break
    
    front += str[b]
    b += 1

  a = 0
  out = ""
  while(a < n):     #loops for n times
    out += front
    a += 1
  return out
