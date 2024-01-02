

import java.util.Scanner ;  
public class BasicAddition {
    
        public static void main(String[] args)
        {
            Scanner input = new Scanner(System.in);
            int num1, num2, sum;

            System.out.println("Enter first number:");
            num1 = input.nextInt();
            System.out.println("Enter second Number: ");
            num2 = input.nextInt();
            sum = num1 + num2;
            System.out.printf("sum = %d\n", sum);
    }
    
}
