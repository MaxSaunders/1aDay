/*
The squirrels in Palo Alto spend most of the day playing. 
In particular, they play if the temperature is between 60 and 90 (inclusive). 
Unless it is summer, then the upper limit is 100 instead of 90. 
Given an int temperature and a boolean isSummer, 
return true if the squirrels play and false otherwise.

squirrelPlay(70, false) → true
squirrelPlay(95, false) → false
squirrelPlay(95, true) → true
*/


public boolean squirrelPlay(int temp, boolean isSummer) {
  int t = temp;
  
  if (isSummer == true){
    if (t >= 60){
      if (t <= 100){
        return true;
      }else{
        return false;
      }
    }else{
      return false;
    }
  }else{
    if (t >= 60){
      if (t <= 90){
        return true;
      }else{
        return false;
      }
    }else{
      return false;
    }
  }
  
}