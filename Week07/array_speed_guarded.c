#include <stdio.h>
#include <stdlib.h>

// TASK: Put your implementation of safe_array here

int main() {
  const int size = 1000000;
  int sum = 0, val;
  scanf("%d", &val);

  array_t *array = make_array(size);
  for (int i = 0; i < size; i++) {
    set(array, i, i);
  }
  for (int j = 0; j < 1000; j++) {
    for (int i = val; i < size - val; i++) {
      set(array, i, get(array, i - 1) + get(array, i + 1));
    }
  }
  for (int i = 0; i < size; i++) {
    sum += get(array, i);
  }
  printf("%d\n", sum);
  destroy_array(array);
}
