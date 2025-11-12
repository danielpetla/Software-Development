#include <stdio.h>

int main() {
  int a, b;

  // This part here reads two numbers from the user
  printf("Enter two numbers: ");
  scanf("%d %d", &a, &b);
  // We will learn about the above in the next lecture

  // Here some computation happens
  int c = 0;
  while (a >= b) {
    a = a - b;
    c = c + 1;
  }

  // This prints the result
  printf("The magic result is %d\n", c);
}

//1. The values of 'a' and 'b' afect the result because while the condition for the while loop is fullfilled the program will keep adding +1 to c
//2. If the inputs are 10 5 -> a = 5 and c = 2 | if 20 3 -> a = 17 and c = 6
//3. It wont work if b is a negative number (a will increase for ever) or if a and b are floating number (because they are intagers). 