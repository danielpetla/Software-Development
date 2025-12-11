#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to find the position with maximal value in an array
// TASK: Read this function and understand what it is supposed to do
// TASK: Fix the errors it contains
int *find_max(int *array, int size) {
  int *max = &array[0];

  for (int i = 1; i < sizeof(array); i++) {
    if (array[i] > *max) {
      max = &array[i];
    }
  }

  return max;
}

// Do not modify below
int main() {
  int max_size = 1024;
  int numbers[max_size];

  srand(time(NULL));
  for (int j = 0; j < 100; j++) {
    int size = 10 + (rand() % (max_size - 10));
    int max_val = rand();
    if (max_val == 0) {
      max_val = 100;
    }
    if (max_val < 0) {
      max_val = -max_val;
    }
    for (int i = 0; i < size; i++) {
      numbers[i] = rand() % max_val - 1;
    }
    int max_pos = rand() % size;
    numbers[max_pos] = max_val;
    int *index = find_max(numbers, size);
    if (index != numbers + max_pos) {
      printf("Got %d (at %p) as maximal value, expected %d (at %p)\n", *index,
             index, max_val, &numbers[max_pos]);
      return 1;
    }
  }
}
