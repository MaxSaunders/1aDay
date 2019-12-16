"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""

def cat_dog(str):
  
  catCount = 0
  dogCount = 0
  
  catCount = str.count('cat')
  dogCount = str.count('dog')
  
  return catCount == dogCount

    
print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))