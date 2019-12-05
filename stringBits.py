"""
Given a string, return a new string made of every other char 
starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""
def string_bits(str):
  out = ""
  a = 0
  while(a < len(str)):
    out += str[a]
    a += 2      #increments to next odd char
  return out
