"""
Given a string, return the count of the number of times 
that the last 2 characters of the string appear in the string
not counting the last 2 characters


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""

def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[len(str)-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i + 2]
    if sub == last2:
      count += 1
  
  return count
