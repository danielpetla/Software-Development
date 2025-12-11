#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char *read_line(){
    char *str = malloc(1);
    int size = 0;
    int c;

    while ((c = getc(stdin)) != '\n'){
         size++;
        str = realloc(str, size + 1); // +1 for null terminator
        str[size - 1] = (char)c;
}
for (int i = 0; i < size/2; i++){ //Reversing the line
        char bank = str[i];
        str[i] = str[size - i - 1];
        str[size -i -1] = bank;
    }

str[size] = '\0'; // null-terminate
    return str;
}


int main (){
    printf("Please enter a string: ");
    char *line = read_line();
    
    printf("Your string reversed is: %s\n", line);
    free(line);
}