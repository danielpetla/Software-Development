#include <stdio.h>
int function(int var) {
  if (var == 0) {
    scanf("%d", &var);
  }
  var += 1;
  printf("%d ", var);
  return 1;
}
int main() {
  int var = 0;
  function(var);
  var += 1;
  function(var);
  printf("%d", var);
}