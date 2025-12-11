#include <stdio.h>
#include <stdbool.h>

int main() {
  int number;
  printf("Please enter a number: ");
  if (!scanf("%d", &number)) { // TASK: Replace the "?" with appropriate instructions
    // Ignore this part
    printf("This is not a number!\n");
    return 1;
  }

  // TASK: Add appropriate if-else statements around these printf-instructions
if (number > 0) {
  printf("The number %d is positive\n", number);
}
else if (number < 0) {
  printf("The number %d is negative\n", number);
}
else {
  printf("The number %d is zero\n", number);
}

}
