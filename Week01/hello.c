#include <stdio.h>

int main() {
    char s[101];       // max 100 chars + null terminator
    scanf("%100s", s); // read the name
    printf("Hello %s!\n", s);
    return 0;
}