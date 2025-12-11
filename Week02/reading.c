#include <stdio.h>

int main() {
  int x, y;
  printf("Please enter two numbers: ");
  // Read x and y from the user
  scanf("%d %d", &x, &y);

  double average = (x - y) / 2;
  double maximum;
  if (x > y) { // We haven't learnt "if" yet
    maximum = x;
  } else {
    maximum = y;
  }

  // Print the response
  printf("The average of %d and %d is %lf\n", x, y, average);
  printf("The maximum is %lf\n", maximum);
}
