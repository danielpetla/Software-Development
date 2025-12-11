#include <stdio.h>

int main (){
    //Implement a simple fraction to decimal converter. 
    int n, m;
    printf("Please selec two numbers: ");
    //Scaning the numbers written in printf
    scanf("%d %d", &n, &m);
    // Converting those 2 intagers in doubles
    double N, M;
    N = n;
    M = m; 
    int fraction = n / m;
    double Fraction = N / M;
    printf("Your fractional number is: Intager = %d Float = %lf\n", fraction, Fraction);
    
}