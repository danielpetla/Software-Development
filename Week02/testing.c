#include <stdio.h>
#include <string.h>


int main (){
   int size = 1024;
char str[size];
for (int i = 0; i < size; i++) {
  char chr;
  scanf("%c", &chr);
  if (chr == '\n') {
    str[i] = '\0';
    break;
  }
  str[i] = chr;
  printf("%s", str);
}
}