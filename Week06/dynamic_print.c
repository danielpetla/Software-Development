#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void print_int_array(int *array, int size) {
  // TASK: Add code that prints the contents of the given array
  for(int i = 0; i < size; i++){
    printf("%d", array[i]);
  }
  printf("\n");
}

int main() {
  // Ignore the part below and do not modify it

  srand(time(NULL));
  int count = 5 + (rand() % 5); // Print between 5 and 10 arrays
  for (int j = 0; j < count; j++) {
    int size = rand() % (j * 10 + 1); // Randomly choose a size between 0 and 100
    int *array = malloc(sizeof(int[size]));
    for (int i = 0; i < size; i++) {
      array[i] = rand() % 100; // Fill the array with random numbers between 0 and 100
    }
    printf("Array #%d: ", j);
    print_int_array(array, size);
    printf("\n");
    free(array);
  }
}
