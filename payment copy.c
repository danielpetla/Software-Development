#include <stdio.h>

int main(){
    int amount;
    printf("Enter an amount: ");
    scanf("%d", &amount);

    //Check if the number can be divided by 20, will show how many 20 bills are needed
    int v20;
    //v20 = how many 20 bills are needed
    v20 = amount / 20;

    printf("20€: %d\n", v20);
// ------------------------------------
//Gets the number after the 20 bills and check if it can be divided by 10, shows how many 10 bills are needed
    int a2, v10;
    // a2 = the amount after the 20€ bills are "used"
    a2 = amount - (20 * v20);
    //v10 = how many 10€ bills are needed
    v10 = a2 / 10;

    printf("10€: %d\n", v10);
// ---------------------------------
    int a3, v5;
    //a3 = the amount after the 10€ bills are "used"
    a3 = a2 - (10 * v10);
    //v5 = how many 5€ bills are needed
    v5 = a3 / 5;

    printf("5€: %d\n", v5);
// ----------------------------------
    int a4, v2;
    a4 = a3 - (5 * v5);
    v2 = a4 / 2;

    printf("2€: %d\n", v2);
// ---------------------------------
    int a5;
    //there is no need for v1 because v1 = a5 always (since we are dividing by 2)
    a5 = a4 - (2 * v2);

    printf("1€: %d\n", a5);
}