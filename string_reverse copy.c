#include <stdio.h>
#include <string.h>

void reverse_string(char str[]) {
  // TASK: Implement this function
  int len = strlen(str);
  for (int i = 0; i < len/2; i++){ // It is len/2 because I'm not replacing a char every turn, I'm swamping them: So by the half of it everything is already in the right place
    //This line stores the character at position i temporarily, because we’re about to overwrite it.
    char bank = str [i];
    //Replace the cahr by its opposite
    str [i] = str[len - 1 - i];
    //Put the cahr that was stored and had just been replace at the position of its opposite
    str[len - 1 - i] = bank; 
  }
}

int main() {
  char hello[] = "hello";
  reverse_string(hello);
  printf("hello reversed is %s\n", hello);
  reverse_string(hello);
  printf("hello is %s\n", hello);

  char bye[] = "bye";
  reverse_string(bye);
  printf("bye reversed is %s\n", bye);
  reverse_string(bye);
  printf("bye is %s\n", bye);
}
