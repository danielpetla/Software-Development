#include <stdio.h>
#include <stdlib.h>

int main() {
  const int size = 1000000;
  int sum = 0, val;
  scanf("%d", &val);

  int *array = malloc(sizeof(int[size]));
  for (int i = 0; i < size; i++) {
    array[i] = i;
  }
  for (int j = 0; j < 1000; j++) {
    for (int i = val; i < size - val; i++) {
      array[i] = array[i - 1] + array[i + 1];
    }
  }
  for (int i = 0; i < size; i++) {
    sum += array[i];
  }
  printf("%d\n", sum);
}
