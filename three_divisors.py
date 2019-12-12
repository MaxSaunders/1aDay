"""
Given a value N. The task is to find how many numbers less than 
or equal to N have numbers of divisors exactly equal to 3.
"""

def three_divisors(n):
  
  total_counter = 0
  
  i = 2
  while(i <= n):
    divisor_count = 0
    
    j = 1
    while(j <= i):
      if ((i % j) == 0):
        divisor_count += 1
      j += 1
    if(divisor_count == 3):
      total_counter += 1
    i += 1
      
  return total_counter
  
print(three_divisors(3))
print(three_divisors(4))
print(three_divisors(6))
print(three_divisors(10))
print(three_divisors(30))