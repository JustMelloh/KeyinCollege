import java.util.Scanner;
import java.util.*;

public class HelloWorld{

    // Attributes
    // Methods
    // Constructors
    // Getter and Setters
    //toString() method


public static void main(String[] args) {
    

    Scanner input = new Scanner(System.in);

    int num1, num2, sum; // Declare Variables

    System.out.print("Enter an integer: ");
    num1 = input.nextInt();
    System.out.print("Enter a second integer: ");
    num2 = input.nextInt();

    sum = num1 + num2;

    System.out.println("The sum is: " + sum);

    System.out.print("*****");
}


}