/*
Given an array of scores sorted in increasing order, 
return true if the array contains 3 adjacent scores that differ 
from each other by at most 2, 
such as with {3, 4, 5} or {3, 5, 5}.
*/


public boolean scoresClump(int[] s) {
  for(int i = 1; i < s.length - 1; i++){
    if(s[i] - s[i - 1] <= 2){
      if(s[i + 1] - s[i] <= 2){
        if(s[i + 1] - s[i - 1] <= 2){
        return true;
        }
      }
    }
  }
  return false;
}
