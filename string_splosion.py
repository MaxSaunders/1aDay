"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

def string_splosion(str):
  out = ""
  str2 = ""
  a = 0
  while(a < len(str)):
    str2 += str[a]  #stores string of chars and adds next char
    out += str2     #adds string of chars to final string
    a += 1
  return out
