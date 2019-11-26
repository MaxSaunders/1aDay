/*
Prcatice in java with searches
*/
import java.util.Arrays;
import java.util.Scanner;
public class Main{
    public static int[] lSearch(int[][] arr, int x){
        for(int i = 0; i < arr[0].length; i++){
            for(int j = 0; j < arr.length; j++){
                if(arr[i][j] == x)
                    return new int[] {i,j};
            }
        }
    
  
    // If element is not present in array 
    return new int[] {-1,-1}; 
    }
    
    
    public static void main(String[] args){
        int[][] num = { {1,4,17,6},{8,18,3,2},{9,19,7,5},{10,20,15,14},{12,21,13,11} };
        int n = num.length;
        int target = 10;
        int result[] = lSearch(num, target);
        //System.out.println(num.length);
        //System.out.println(num[0].length);
        if (result[0] = -1)  
            System.out.println("Element (" +target+ ") is not present in array");
        else    
            System.out.println("Element (" +target+ ") is present at index: " +result);
}
}