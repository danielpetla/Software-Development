#include <stdio.h>

void print_array(int *array, int size) {
  // TASK: Put printing code here
  for(int i = 0; i < size; i++){
    printf("%d, ", array[i]);
  }
  printf("\n");
}
