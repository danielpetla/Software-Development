#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <stdlib.h>

//Function to see the difference between the number and the guess
void compare(int user_number, int number){
if(user_number > number){
    printf("This number is too large\n");
}
else if (user_number < number) {
    printf("This number is too low\n");
}
else {
    printf("Correct!");
}
}

// TASK: Compare number and user_number, indicate whether the user is correct or
int main() {
    // Selecting the range for the random number
    int range;
    printf("Select the range size: ");
    scanf("%d",&range);
  // The following two lines get a (sort of) random number 0 - 9
  srand(time(NULL));
  int number = rand() % range;

//Variable to store how many chances the player has left
int chances;
printf("How many chances you want? ");
scanf("%d", &chances);


// Actual game loop
  int user_number;
  while(chances > 0){
    printf("Please enter your guess (%d chances left): ", chances);
  scanf("%d", &user_number);

  if (user_number == number){
    printf("Correct!\n");
  printf("My number was %d!\n", number);
  return 0;
  }
  else{
    compare(user_number, number);
    chances --;
  }
  }
  printf("No more chances, sorry!\n");
  return 0;
}