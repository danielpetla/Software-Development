#include<stdio.h>
#include<stdlib.h>

typedef struct listElement{
    int data;
    struct listElement* next;
} listElement;

typedef struct list{
    listElement* head;
} list;


listElement* new_element(int value, int* next){
    listElement* new_element = malloc(sizeof(listElement));
    new_element->data = value;
    new_element->next = next;
    return new_element;
}

list* creat_list(){
    list* L = malloc(sizeof(list));
    listElement* second = new_element(0, NULL);
    L->head->data = 1;
    L->head->next = second;

    return L;
}

int main (){
    int n = 0;
    list* L;
    list* M;
    printf("Insert a number please: ");
    scanf("%d", &n);
    
    L = creat_list();
    
}