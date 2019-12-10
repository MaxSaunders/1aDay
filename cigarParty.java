/******************************************************************************

When squirrels get together for a party, they like to have cigars. A squirrel party is successful 
when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which 
case there is no upper bound on the number of cigars. Return true if the party with the given 
values is successful, or false otherwise.

*******************************************************************************/
public class Main
{
	public static boolean cigarParty(int cigars, boolean isWeekend){
    	if (cigars >= 40){
            if (cigars <= 60){
                System.out.println("True");
                return true;
                }
            else if (isWeekend == true){
                System.out.println("True");
                return true;
                }
            else{
                System.out.println("False");
                return false;
                }
        }
        else{
          System.out.println("False");
            return false;
    	    }
        }

    public static void main(String[] args){
		cigarParty(30, false);
		cigarParty(50, false);
		cigarParty(70, true);
		
	}
}
