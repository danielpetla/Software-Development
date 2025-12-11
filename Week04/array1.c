#include <stdio.h>
#include <stdbool.h>
int main() {
  int size = 10;
  double arr[size];
  double num = 0;
  printf("Enter a number: ");
  scanf("%lf", &num);
  if (num < 0){
    printf("Need a positive number!");
    num = 1;
  }

  // Here num is positive because of the check above
  for (int i = 0; i < size; i++) {
    arr[i] = (num - 1) * (i + 1);
  }

  double mult = 1;
  for (int i = 1; i <= size; i ++) {
    mult *= arr[i - 1];
  }
  printf("The result is %lf\n", mult);
}
