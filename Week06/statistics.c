// TASK: Add required includes
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int *read_array(int size) {
  // TASK: Allocate an integer array of sufficient size
  int *values = malloc((size + 1) * sizeof(int));
  // TASK: Read the integers
  for (int i = 0; i < size; i++){
    printf("Enter value %d: ", i);
    scanf("%d", &values[i]);
  }

return values;
}

double compute_average(int *array, int size) {
  // TASK: Compute the average
  int sum = 0;
  for (int i = 0; i < size; i++){
    sum = sum + array[i];
  }
  double SUM = sum;
  double SIZE = size;
  double avg = SUM / SIZE;

  return avg;
}

int main() {
  int size;
  printf("Enter number of values: ");
  scanf("%d", &size);
  int *array = read_array(size);
  double avg = compute_average(array, size);
  printf("Average: %lf\n", avg);

  // TASK: Free array
  free (array);
  array = NULL;
}
