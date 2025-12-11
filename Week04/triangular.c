#include <stdio.h>

int main (){
    int n;
    printf("Please Enter a Number: ");
    scanf("%d", &n);
    int add = 0;
    for(int i = 1; i < n; i++) {
        //It is getting the numbers before n, ex: n-1, n-2, n-3 ...
        int m = n - i;
        //storing the sum of the numbers taht come before n
        add = add + m;
    }
    // The triangular number: (the sum of all numbers from 1 to n)
    int sum = n + add;
    printf("Your triangular number = %d\n", sum);
}