#include <stdio.h>

// TASK: Define your struct here and define a type alias
typedef struct student {
  int id;
  int year;
  double grade;
  // Should contain id (int), year (int), and grade (double)
} student;

int main() {
  // TASK: Declare a variable of your defined type
  student A; // A Is a student type struct

  // TASK: Ask the user to input the student data
  printf("Please enter student data:\n");
  scanf("%d %d %lf", &A.id, &A.year, &A.grade);
  printf("ID: %d ", A.id);

  printf("Year: %d ", A.year);

  printf("Grade: %lf\n", A.grade);

  // TASK: Print the information back to the user
}

