import java.util.Scanner;


public class HelloWorld {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String str = "";
        if (scanner.hasNextLine()){
            str = scanner.nextLine();
        }
        System.out.printf("Hello, %s%n", str);  // %n = \n (in C)
    }
}
