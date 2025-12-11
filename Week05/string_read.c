#include <stdio.h>
#include <string.h>

int read_string(char destination[], int limit) {
  // TASK: Implement this function
  for (int i = 0; i < limit - 1; i++){
    char chr = getc(stdin);

  if (chr == '\n'){
    destination [i] = '\0';
    return i;
  }
  destination[i] = chr;
  }

  return 0;
  // Hint: Use char chr = getc(stdin) to get a single character from the standard input
  // Hint: Check if the read char is equal to \n to detect that the user finished a line of input
}

int main() {
  int size = 1024;
  char buffer[size];

  printf("Please enter a string: ");
  int length = read_string(buffer, size);
  if (strlen(buffer) == length) {
    printf("Your string is %ld (== %d) long and is: %s\n", strlen(buffer), length, buffer);
  } else {
    printf("Something went wrong -- your string is %s\n", buffer);
  }
}
