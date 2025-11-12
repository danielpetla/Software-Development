#include <stdio.h>
#include <stdbool.h>

int main() {
  double fahrenheit;
  // This part here reads a number from the user
  printf("Enter Fahrenheit: ");
  scanf("%lf", &fahrenheit);
  // We will learn about the above in the next lecture
  double celsius;
  celsius = (fahrenheit -32) / 1.8;




  printf("Value in Celsius: %lf\n", celsius);
}
