#include <stdio.h>
#include <stdbool.h>

// This function computes how many digits a number has
int digits(int number) {
  int digits = 0;
  while (number > 0) {
    digits += 1;
    number /= 10;
  }
  return digits;
}

int main() {
  // TASK: Read a number from the user
  int number;
  printf("Enter a PIN: ");
  scanf("%d", &number);
  //In this part I'm checking if the number is positive and if it is I call the digits function to check the number of digits
  if (number > 0){
    int numb_digits = digits (number);
    if (numb_digits == 5){
      int five_digit_sum;
      // Now I get the module (%) that will give me the remainder fo (in this case) a division by 10 | by dividing the numbers before the module I can get the nest char
      int numb1 = number%10;
      int numb2 = (number/10)%10;
      int numb3 = (number/100)%10;
      int numb4 = (number/1000)%10;
      int numb5 = (number/10000)%10;
      five_digit_sum = numb1 + numb2 + numb3 + numb4 + numb5;
      // Now I check if the sum is divisable by 7 (I check this by seeing if the remainder is == 0)
      if (five_digit_sum % 7 == 0 ) {
        printf ("Your PIN is acceptable!\n");
      }
      else {
        printf("Not acceptable PIN\n");
      }

    }
    else {
      printf("Please enter a valid PIN\n");
    }
  }
  else {
    printf("No negative numbers allowed! Please a valid number\n");
  }
}
