#include<stdio.h>
#include<stdlib.h>


typedef struct array
{
    int size;
   int data[]; 
}array;

array* create_array(int size){
    array* arr = malloc(sizeof(array) + size * sizeof(int));
    arr->size = size;

    return arr;
}

void set_value(array* arr, int i, int value){
    if (i >= 0 && i < arr->size) {
        arr->data[i] = value;
        printf("Okay!\n");
    }
    else{
        printf("Illegal index %d\n", i);
    }
}

void print(array* arr){
    for(int i = 0; i < arr->size; i++){
        printf("%d ", arr->data[i]);
    }
    printf("\n");
}

void sum(array* arr){
    int sum = 0;
    for(int i = 0; i < arr->size; i++){
        sum = sum + arr->data[i];
    }
    printf("%d\n", sum);
}


int main (){
    int v1 = 0, v2 = 0;
    char command;
    array* arr = NULL;
    while(1){
        printf("Command: ");
        scanf(" %c", &command);

        if (command == 'b'){
            break;
        }

        if(command == 'c'){
            scanf("%d", &v1);
            if (arr != NULL) free(arr); 
            arr = create_array (v1);
            printf("Created an array of size %d!\n", arr->size);
    }
        if(command == 's'){
            scanf("%d %d", &v1, &v2);
            if (arr != NULL) {
                set_value(arr, v1, v2);
        }
    }

        if (command == 'p'){
            print(arr);
        }
        if (command == 't'){
            sum(arr);
        }
}
    free (arr);
}