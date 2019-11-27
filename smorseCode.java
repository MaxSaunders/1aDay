/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

public class Main
{
    public static String convert(char c){
        switch (c){
            //.--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
            case 'a':
                return ".-|";
            case 'b':
                return "-...|";
            case 'c':
                return "-.-.|";
            case 'd':
                return "-..|";
            case 'e':
                return ".|";
            case 'f':
                return "..-.|";
            case 'g':
                return "--.|";
            case 'h':
                return "....|";
            case 'i':
                return "..|";
            case 'j':
                return ".---|";
            case 'k':
                return "-.-|";
            case 'l':
                return ".-..|";
            case 'm':
                return "--|";
            case 'n':
                return "-.|";
            case 'o':
                return "---|";
            case 'p':
                return ".--.|";
            case 'q':
                return "--.-|";
            case 'r':
                return ".-.|";
            case 's':
                return "...|";
            case 't':
                return "-|";
            case 'u':
                return "..-|";
            case 'v':
                return "...-|";
            case 'w':
                return ".--|";
            case 'x':
                return "-..-";
            case 'y':
                return "-.--|";
            case 'z':
                return "--..";
        }
        return "";
    }
    
    public static String smorse(String p){
        //needs to convert string input to array to increment through 
        //and convert each char to morse with if statement case 
        String morse = "";
        
        for(int i = 0; i < p.length(); i++){
            morse += convert(p.charAt(i));
        }
            
        
        return morse;
    }
    
    
    public static void main(String[] args){
	System.out.println(smorse("sos"));// => "...---..."
    System.out.println(smorse("daily"));// => "-...-...-..-.--"
    System.out.println(smorse("programmer"));// => ".--..-.-----..-..-----..-."
    System.out.println(smorse("bits"));// => "-.....-..."
    System.out.println(smorse("three"));// => "-.....-..."
    
    }
}
