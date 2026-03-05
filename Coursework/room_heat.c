#include<stdio.h>
#include<stdlib.h>

int main(){
    int n, m, k;

    if (scanf("%d %d %d", &n, &m, &k) != 3)
        return 1;

    int **pipes = malloc(m * sizeof(int *));
    int *pipe_sizes = malloc(m * sizeof(int));


    for (int i = 0; i < m; i++) {
        int num_rooms;
        scanf("%d", &num_rooms);

        pipe_sizes[i] = num_rooms;
        pipes[i] = malloc(num_rooms * sizeof(int));

        for (int j = 0; j < num_rooms; j++) {
            scanf("%d", &pipes[i][j]);

        }

    }
}
