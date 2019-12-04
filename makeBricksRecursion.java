/******************************************************************************

We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return true if it is possible to make the goal by choosing from the given bricks. 

makeBricks(3, 1, 8) → true
makeBricks(3, 1, 9) → false
makeBricks(3, 2, 10) → true

*******************************************************************************/
public class Main
{
    
public static boolean makeBricks(int small, int big, int goal) {
    
    if (goal == 0){
        return true;
    }else if(goal != 0 && small == 0 && big == 0){
        System.out.println("1");
        return false;
    }else if(goal < 5 && small < goal){
        return false;
    }else if(goal > (big * 5) + small){
        return false;
    }
    if (goal >= 5 && big >= 1){
        if(makeBricks(small, big - 1, goal - 5) == true){
            return true;   
        }
    }
    if (goal >= 1 && small >= 1){
        if(makeBricks(small - 1, big, goal - 1) == true){
            return true;
        };
    }
    System.out.println("2");
    if(goal != 0){
        return false;
    }else{
        return true;
    }
}
  
	public static void main(String[] args) {
		System.out.println(makeBricks(3,1,8));
		System.out.println(makeBricks(3,1,9));
		System.out.println(makeBricks(3,2,10));
	}
}
