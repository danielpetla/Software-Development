import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
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
            double div = (double) first / second;
            System.out.printf("%.2f%n", div);
        }
    }
}
