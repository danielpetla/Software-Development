import java.util.Scanner;
import java.util.InputMismatchException; // Needed to catch bad input

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try{
            System.out.print("Please enter: ");
            double first = scanner.nextDouble();
            String operation = scanner.next();
            double second = scanner.nextDouble();

            // TODO Compute and print the result

            if (operation.equals("+")){
                double sum = (double) first + second;
                System.out.printf("%.2f%n", sum);
                }
            else if (operation.equals("-")){
                double sub = (double) first - second;
                System.out.printf("%.2f%n", sub);
            }
            else if (operation.equals("*")){
                double mul = (double) first * second;
                System.out.printf("%.2f%n", mul);
            }
            else if (operation.equals("/")){
                if (second == 0){
                    throw new ArithmeticException("Division by zero is not allowed");
                }
                    double div = (double) first / second;
                    System.out.printf("%.2f%n", div);
                }
            }
        catch(InputMismatchException e){
            System.out.println("Error: Please enter valid numbers.");
        }
    }
}
