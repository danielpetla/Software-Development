#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <stdlib.h>

int main() {
  // The following two lines get a (sort of) random number 0 - 9
  srand(time(NULL));
  int number = rand() % 10;

  int user_number;
  printf("Please enter your guess: ");
  scanf("%d", &user_number);
  // TASK: Read the guess of the user

// TASK: Compare number and user_number, indicate whether the user is correct or
if (user_number == number) {
  printf("Correct!\n");
  printf("My number was %d !", number);
}
else {
  printf("Incorrect!\n");
  printf("My number was %d\n", number);
}
}
