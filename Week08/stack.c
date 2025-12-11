#include <stdlib.h>
#include<stdio.h>

// TASK: Define a struct for the stack and introduce the type alias stack_t
typedef struct stack
{
  int* bellow;
  int size; // capacity
  int count; // number of elements
  int* data; // pointer to dynamic array
} Stack_t;


// TASK: Implement the required functions:

Stack_t *make_stack(){
  Stack_t* s = malloc(sizeof(Stack_t));
  s->bellow = NULL;
  s->count = 0;
  s->size = 1;
  s->data = malloc(sizeof(int) * s->size);
  return s;
}

void destroy_stack(Stack_t *stack){
  free(stack->data);
    free(stack);
}

int size(Stack_t *stack){
  return stack->count;
}

void push(Stack_t *stack, int value){
  stack->size = stack->size + 1;
  stack->count++;
  stack->data = realloc(stack->data, sizeof(int) * stack->size);
  stack->data[stack->count] = value;

  if(stack->count != 1){
    stack->bellow = &stack->data[stack->count - 1];
  }
}

int pop(Stack_t *stack){
  int pop = stack->data[stack->count];
  stack->data[stack->count] = 0;
  stack->count--;
  stack->size = stack->size - 1;

  return pop;
}

// Do not modify below!

void fail(char msg[]) {
  printf("%s", msg);
  exit(1);
}

int main() {
  printf("Testing stack implementation\n");
  Stack_t *s = make_stack();
  if (size(s) != 0) {
    fail("Size is wrong!");
  }
  push(s, 1);
  push(s, 2);
  if (size(s) != 2) {
    fail("Size is wrong!");
  }
  if (pop(s) != 2) {
    fail("Push / Pop is wrong!");
  }

  printf("Pushing many elements\n");
  printf("If this is slow, there probably is something wrong\n");
  const int size = 1000000;
  srand(0);
  int array[size];
  for (int i = 0; i < size; i++) {
    int value = rand();
    array[i] = value;
    push(s, value);
    if (pop(s) != value) {
      fail("Push / Pop is wrong!");
    }
    push(s, value);
  }
  for (int i = size - 1; i >= 0; i--) {
    if (pop(s) != array[i]) {
      fail("Push / Pop is wrong!");
    }
  }
  destroy_stack(s);
  printf("Done!\n");
}
