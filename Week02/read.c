#include <stdio.h>

int main (){
    int x;
    printf("Please enter a number: ");
    // Read x from the user
    scanf("%d", &x);

    int timestwo = x * 2;
    //Dobles the value of x and stores it on the variable "timestwo"
    printf("%d times 2 is %d\n", x, timestwo);
}
