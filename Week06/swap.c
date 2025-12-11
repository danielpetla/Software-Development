#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b) {
  // TASK: Implement swapping the values of a and b here.
  int bank = *a;
  *a = *b;
  *b = bank;
}

// Do not modify below
int main() {
  srand(time(NULL));
  for (int j = 0; j < 100; j++) {
    int a = rand();
    int b = rand();
    int c = a;
    int d = b;
    swap(&a, &b);
    if (a != d || b != c) {
      printf("Swapping %d and %d failed\n", c, d);
      return 1;
    }
  }
  printf("All tests passed.\n");
}
