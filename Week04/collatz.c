#include <stdio.h>

int main (){
    int n;
    printf("Please Select a number: ");
    scanf("%d", &n);
while(1){
    if (n % 2 == 0){
     n = n/2;
     printf("%d -> ", n);
    }
    //Checking if the result is finally one to end the while loop
    if (n == 1){
        break;
    }

    if (n % 2 != 0){
     n = (3*n) + 1;
     printf("%d -> ", n);
    }
    if (n == 1){
        break;
    }
}
printf("That is it!\n");
}