#include <stdio.h>
#include <stdbool.h>

int main() {
    int conversion;
    int again;
    again = 2;
    while(again == 2) {
    printf("Wich conversion do you want (1/2): ");
    scanf("%d", &conversion);

    if (conversion == 1) {
        double fahrenheit;
        // This part here reads a number from the user
        printf("Enter Fahrenheit: ");
        scanf("%lf", &fahrenheit);
        // We will learn about the above in the next lecture
        double celsius;
        celsius = (fahrenheit -32) / 1.8;
        printf("Value in Celsius: %lf\n", celsius);
    }
    else if (conversion == 2) {
        double cel;
        printf("Enter Celcius: ");
        scanf("%lf", &cel);

        double fa;
        fa = (cel * 1.8) + 32;  
        printf("Value in Fahrenheit: %lf\n", fa);
    }
    printf ("Continue ?(y/n) ");
    scanf ("%d", &again );
}

    printf("Okay, Bye!\n");
return 0;
}
