import java.util.*;
/*
 Max Saunders

Vignere Cipher
 */
public class Main
{

public static String encryption(String text, String key)
{
String enc_string = "";
text = text.toUpperCase();

	for (int counter = 0, x = 0; counter < text.length(); counter++)
	{
    
    char characters = text.charAt(counter);
    
	if (text.charAt(counter) == '.') //Checks for punctuation
	{
		enc_string += '.'; //Recreates period in ecrypted message
		System.out.print(" ");
	}
	
	if (text.charAt(counter) == ' ') //Checks for spaces and recreates them in the newKey and ecrypted message
	{
		enc_string += ' ';
		System.out.print(" ");
	}
	
    if (characters < 'A' || characters > 'Z')// this makes it so the code only looks for values between A and Z this ignores spaces and punctuation
    continue;              

        enc_string += (char) ((characters + key.charAt(x) - 2 * 'A') % 26 + 'A');// algorithm for cipher
		
		System.out.printf(""+key.charAt(x));
		
       x = ++x % key.length();
	
	}
	
return enc_string;
}   

public static String decryption(String text, String key)
{
	String dec_string = "";
	
	for (int counter = 0, x = 0; counter < text.length(); counter++)
	{
    
    char characters = text.charAt(counter);
    
	if (text.charAt(counter) == '.')
	{
		dec_string += '.';
	}
	
	if (text.charAt(counter) == ' ')
	{
		dec_string += ' ';
	}
	
    if (characters < 'A' || characters > 'Z')// this makes it so the code only looks for values between A and Z this ignores spaces and punctuation
    continue;              

        dec_string += (char) ((characters - key.charAt(x) + 2 * 'A') % 26 + 'A');// algorithm for cipher
       x = ++x % key.length();
	}
	
return dec_string;
	
}

public static void main(String[] args) 
    {

String key = "SAUNDERS";
        
Scanner sc=new Scanner(System.in);//get message 
System.out.println("Enter the message: ");

String plain_text =sc.nextLine();

        System.out.println("=========================================================================");
		System.out.println("The keyword is:        "+key);
		System.out.println("The message is:        " +plain_text);
		System.out.printf("The new key is:        "); //prints out key changed to the length of the message
		
String cipher_text = encryption(plain_text, key);//start 
        System.out.println("\n\nThe encrypted message: "+cipher_text+ "\n"); //print out encrypted message
		
		//Hope you like the formatting!
		
String decoded_message = decryption(cipher_text, key);
		System.out.println("The decrypted message: " +decoded_message); //print out encrypted message after it has run through decryption
        System.out.printf("=========================================================================");
    
	// I included the decryption feature as a bonus to show that the process can be reversed
	
    }
     
}
