#include<stdio.h>

int main(){
int n;
// x = F0 and y = F1
int x = 0;
int y = 1;
int z = 0;
printf("Please enter a number: ");
scanf("%d", &n);
printf("0 ");
int F = 1;

while(1){
   z = x + y; //Fa
    printf("%d ", z);
    F++;
    if (F > n){
        break;
    }  

   y = z + x;//Fa+1
      printf("%d ", y);
      F++;
      if (F > n){
        break;
    }  

   x = z + y;//Fa+2
      printf("%d ", x);
      F++;
      if (F > n){
        break;
    }  
}
printf("\n");
}