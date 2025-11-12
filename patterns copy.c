#include<stdio.h>

int main (){
    int r;
    int i;
    printf ("How many rows would you like ? ");
    scanf("%d", &r);

    int star = r + 2;
    int lastr;
    for (i = 0; i < r; i++){
        if (i == r - 1){
            for ( lastr = 0; lastr <= star; lastr++)
            printf("* ");
        }
        printf("*\n");
    }
    printf("\n");
}