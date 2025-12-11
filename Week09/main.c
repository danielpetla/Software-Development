#include "util.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
  int n;
  scanf("%d", &n);
  int *array = malloc(sizeof(int[n]));
  for (int i = 0; i < n; i++) {
    scanf("%d", &array[i]);
  }

  print_array(array, n);

  free(array);
}
