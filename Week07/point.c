#include <stdio.h>
#include <stdlib.h>

typedef struct point {
  int x;
  int y;
  // TASK: Define the struct
} point_t;

void print_point(point_t *p) {
  // TASK: Print x and y coordinate of p
  //point_t *p -> received the address of read/R and now is also a pointer to the struct r
  printf ("%d,%d", p->x, p->y);
}

point_t *create_point(int x, int y) {
  // TASK: Allocate space for a point and set its coordinates
  point_t* p = (point_t*)malloc(sizeof(point_t)); //Pointer to the instruct contained inside the malloc - the allocated memory is the struct
  p->x = x;
  p->y = y;

  return p;
}

point_t *read_point() {
  // TASK: Read a point from the user
  point_t r; //It is a instruct
  scanf("%d %d", &r.x, &r.y);
  point_t*R = &r;
  return R;
}


// Do not modify below
int main() {
  srand(0);
  for (int i = 0; i < 1000; i++) {
    int x = rand();
    int y = rand();
    point_t *p = create_point(x, y);
    if (p->x != x || p->y != y) {
      printf("Create is wrong");
      exit(1);
    }
    free(p);
  }

  printf("Please enter two coordinates: ");
  point_t *read = read_point();// Now the pointer read = the pointer R
  printf("You entered: ");
  print_point(read);
  printf("\n");
}
