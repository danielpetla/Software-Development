#include <stdio.h>
#include <stdbool.h>

int main() {
  char cha;
  printf("Please enter a character: ");
  scanf("%c", &cha);
  
  int n = cha;
  printf("%d\n", n);


  // TASK: Read a character from the user and print that character's ASCII code
int num;
  printf("Please enter a number: ");
  scanf("%d", &num);

  char ascii = num;
  printf("%c\n", ascii);

  // TASK: Read a number from the user and print the corresponding ASCII character
  // Optional: Validate the input (the number should be a valid ASCII code)
  // Optional: Also print the next smaller and next larger character
}
